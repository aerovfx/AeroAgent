# ==========================
# Python Full Quiz Crawler - Multithreaded
# ==========================

# --------------------------
# 1. IMPORT + LOAD .ENV
# --------------------------
import os
import re
import json
import time
import random
import hashlib
import requests
import cloudscraper
from bs4 import BeautifulSoup, Comment, NavigableString
from urllib.parse import urljoin, urlparse
from collections import defaultdict
from typing import List, Dict, Any
from datasets import Dataset, load_dataset, concatenate_datasets
from huggingface_hub import login, create_repo, upload_file
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
import threading
import logging

# Load .env từ cấp trên của thư mục src
dotenv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".env")
)
load_dotenv(dotenv_path)

# CONFIG
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}
HF_TOKEN = os.getenv("HF_TOKEN")
HF_REPO = os.getenv("HF_REPO")
MERGE_STRATEGY = "smart_merge"  # append / replace / smart_merge
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "2"))  # Số luồng tối đa

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Thread-safe lock cho việc ghi dữ liệu
data_lock = Lock()

# --------------------------
# 2. KHAI BÁO CRAWL FUNCTION
# --------------------------
def make_scraper():
    """Tạo scraper riêng cho mỗi thread"""
    return cloudscraper.create_scraper(browser={'custom': USER_AGENT})

# --------------------------
# SMART CLEANING SYSTEM
# --------------------------

class SmartTextCleaner:
    """Hệ thống lọc nhiễu thông minh với multi-layer pipeline"""
    
    def __init__(self):
        # Smart regex patterns - tổng quát, bao quát nhiều biến thể
        self.patterns = {
            # 1. Tiêu đề bài tập/trắc nghiệm
            'title_patterns': [
                r'(Trắc\s*nghiệm|Bài\s*tập|Đề\s*thi|Kiểm\s*tra|Ôn\s*tập|Chuyên\s*đề)\s+[^:]*\s*\(?có\s*đáp\s*án\)?\s*:?\s*',
                r'(Quiz|Test|Exam|Practice|Review)\s+[^:]*\s*\(?with\s*answer\)?\s*:?\s*',
            ],
            
            # 2. Thông tin môn học/chương  
            'subject_patterns': [
                r'(Bài|Chương|Phần|Lesson|Chapter|Part)\s+\d+\s*[:.]\s*[^:\n]*?(?=\n|$)',
                r'(Kết\s*nối\s*tri\s*thức|Chân\s*trời\s*sáng\s*tạo|Cánh\s*diều|Connect\s*Knowledge)\s*',
                r'(Vật\s*[Ll]í|Toán|Hóa|Sinh|Văn|Anh|Math|Physics|Chemistry|Biology)\s*\d{1,2}\s*',
            ],
            
            # 3. Thông tin đáp án/giải thích
            'answer_patterns': [
                r'(Đáp\s*án|Answer|Giải\s*thích|Explanation|Lời\s*giải|Solution|Hướng\s*dẫn\s*giải)\s*:?\s*[A-D]?\s*',
                r'(Hiển\s*thị|Xem|View|Show|Click|Bấm|Nhấn)\s+(đáp\s*án|answer)\s*',
            ],
            
            # 4. Điều hướng & lựa chọn
            'navigation_patterns': [
                r'Chọn\s+[A-D]\s+Câu\s+\d+\s*[:\s]*',
                r'(Câu\s*)?(trước|sau|Previous|Next)\s*',
                r'(Trang|Page)\s+\d+\s*',
            ],
            
            # 5. Metadata  
            'metadata_patterns': [
                r'(ID|Mã\s*đề|Code)\s*:\s*\w+\s*',
                r'(Thời\s*gian|Time)\s*:\s*\d+\s*(phút|minutes?)\s*',
                r'(Ngày|Date)\s*:\s*\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}\s*',
                r'(Tác\s*giả|Author)\s*:\s*[^:\n]+',
            ],
            
            # 6. Đánh giá/phân loại
            'evaluation_patterns': [
                r'(Độ\s*khó|Difficulty|Mức\s*độ|Level)\s*:\s*[^:\n]+',
                r'(Điểm|Score|Point)\s*:\s*\d+(\.\d+)?\s*',
                r'(Loại|Type|Phân\s*loại|Category)\s*:\s*[^:\n]+',
            ],
            
            # 7. Số thứ tự/ký hiệu (chỉ áp dụng ở đầu dòng)
            'numbering_patterns': [
                r'^\d+\.\s*',
                r'^[A-D]\)\s*',
                r'^\*{3,}\s*',
                r'^#{3,}\s*',
                r'^-{3,}\s*',
            ]
        }
        
        # Blacklist keywords cho validation
        self.question_blacklist = [
            'hiển thị', 'xem đáp án', 'click', 'bấm', 'show answer', 'view answer',
            'chọn đáp án', 'choose answer', 'trang', 'page', 'câu trước', 'câu sau'
        ]
        
        self.option_blacklist = [
            'xem đáp án', 'view answer', 'click', 'bấm', 'hiển thị'
        ]

    def normalize_text(self, text: str) -> str:
        """Layer 0: Chuẩn hóa text cơ bản"""
        if not text:
            return ""
        
        # Normalize whitespace và special chars
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\t+', ' ', text)
        
        # Normalize quotes và dashes
        text = re.sub(r'[“„”‘‚’]', '"', text)   # tất cả dấu nháy kiểu ngoặc kép và đơn → "
        text = re.sub(r'[–—―]', '-', text)       # tất cả dash dài → -

    
        
        
        # Remove excessive punctuation
        text = re.sub(r'[.]{3,}', '...', text)
        text = re.sub(r'[!]{2,}', '!', text)
        text = re.sub(r'[?]{2,}', '?', text)
        
        return text.strip()

    def remove_unwanted_sections(self, text: str) -> str:
        """Layer 1: Loại bỏ sections không mong muốn bằng smart patterns"""
        
        # Áp dụng tất cả pattern categories
        for category, patterns in self.patterns.items():
            if category == 'numbering_patterns':
                continue  # Xử lý riêng cho numbering
                
            for pattern in patterns:
                # Case insensitive, multiline matching
                text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.MULTILINE)
        
        # Xử lý numbering patterns (chỉ ở đầu dòng)
        for pattern in self.patterns['numbering_patterns']:
            text = re.sub(pattern, '', text, flags=re.MULTILINE)
        
        return text

    def is_valid_question(self, question: str) -> bool:
        """Layer 2: Validate câu hỏi hợp lệ"""
        if not question or len(question.strip()) < 15:
            return False
        
        question_lower = question.lower()
        
        # Kiểm tra blacklist
        if any(keyword in question_lower for keyword in self.question_blacklist):
            return False
        
        # Kiểm tra có ít nhất 3 từ có nghĩa
        words = [w for w in question.split() if len(w) > 2 and not w.isdigit()]
        if len(words) < 3:
            return False
        
        # Loại bỏ câu chỉ có số hoặc ký tự đặc biệt
        if question.replace(' ', '').isdigit():
            return False
        
        # Phải có ít nhất 50% ký tự là chữ cái
        alpha_ratio = sum(c.isalpha() for c in question) / len(question)
        if alpha_ratio < 0.5:
            return False
            
        return True

    def is_valid_option(self, option: str) -> bool:
        """Layer 2: Validate đáp án hợp lệ"""
        if not option or len(option.strip()) < 3:
            return False
        
        option_lower = option.lower()
        
        # Kiểm tra blacklist
        if any(keyword in option_lower for keyword in self.option_blacklist):
            return False
        
        # Loại bỏ option chỉ có số hoặc ký tự đặc biệt
        if option.replace(' ', '').isdigit():
            return False
        
        # Phải có ít nhất 30% ký tự là chữ cái
        alpha_ratio = sum(c.isalpha() for c in option) / len(option)
        if alpha_ratio < 0.3:
            return False
            
        return True

    def final_cleanup(self, text: str) -> str:
        """Layer 3: Cleanup cuối cùng"""
        if not text:
            return ""
        
        # Remove markdown remnants
        text = re.sub(r'[*]{1,3}([^*]+)[*]{1,3}', r'\1', text)
        text = re.sub(r'[_]{1,3}([^_]+)[_]{1,3}', r'\1', text)
        text = re.sub(r'#{1,6}\s*', '', text)
        
        # 1. Loại bỏ các dấu câu ở đầu dòng
        text = re.sub(r'^[:.,-]+\s*', '', text)

        # 2. Loại bỏ các dấu câu lặp liên tiếp trong text
        text = re.sub(r'\s*[:.,-]{2,}\s*', ' ', text)

        # 3. Chuẩn hóa khoảng trắng
        text = re.sub(r'\s+', ' ', text).strip()

def hash_text(text: str) -> str:
    """Tạo unique id từ text"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def fetch_html(url: str) -> str:
    """Thread-safe fetch HTML"""
    scraper = make_scraper()  # Mỗi thread có scraper riêng
    try:
        res = scraper.get(url, timeout=60)
        res.raise_for_status()
        res.encoding = 'utf-8'
        return res.text
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        raise

def extract_sub_links(html: str, base_url: str) -> List[str]:
    """Trích xuất các link con từ trang chính"""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    
    # Tìm tất cả các link có chứa "trac-nghiem" hoặc "bai-hoc"
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Kiểm tra nếu link có chứa trắc nghiệm
        if any(keyword in href.lower() for keyword in ['trac-nghiem', 'bai-hoc', 'quiz']):
            # Tạo absolute URL
            full_url = urljoin(base_url, href)
            
            # Loại bỏ các link không mong muốn
            if not any(unwanted in full_url.lower() for unwanted in ['#', 'javascript:', 'mailto:']):
                links.append(full_url)
    
    # Loại bỏ duplicate
    return list(set(links))

def parse_quiz(html: str) -> List[Dict[str, Any]]:
    """Parse quiz từ HTML với smart cleaning system"""
    soup = BeautifulSoup(html, "html.parser")

    # Xóa script, style, comment
    for el in soup(['script', 'style']):
        el.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    quizzes = []
    full_text = soup.get_text("\n", strip=False)
    
    # Apply smart cleaning trước khi parse
    full_text = text_cleaner.remove_unwanted_sections(full_text)
    
    # Enhanced quiz patterns
    quiz_patterns = [
        # Pattern 1: Standard format với "Câu X:"
        r'(?:Câu\s*\d+\s*[:.]\s*(?:\*\*)?)?(.+?)\s*(?=A\.|A\.)\s*A\.\s*(.+?)\s*B\.\s*(.+?)\s*C\.\s*(.+?)\s*D\.\s*(.+?)(?=\nCâu|\n\d+\.|$)',
        
        # Pattern 2: Không có prefix, trực tiếp câu hỏi
        r'([^\n]+?[?.])\s*\n\s*A\.\s*([^\n]+?)\s*\n\s*B\.\s*([^\n]+?)\s*\n\s*C\.\s*([^\n]+?)\s*\n\s*D\.\s*([^\n]+?)(?=\n[^\s]|\n\n|$)',
        
        # Pattern 3: Format compact
        r'(.{20,}?)\s*A\.\s*(.{5,}?)\s*B\.\s*(.{5,}?)\s*C\.\s*(.{5,}?)\s*D\.\s*(.{5,}?)(?=\n|$)',
        
        # Pattern 4: Multi-line questions
        r'([^\n]*[?.](?:\s*\n\s*[^\nA-D].*?)*?)\s*\n\s*A\.\s*([^\n]+?)\s*\n\s*B\.\s*([^\n]+?)\s*\n\s*C\.\s*([^\n]+?)\s*\n\s*D\.\s*([^\n]+?)(?=\n|$)'
    ]
    
    # Thử từng pattern với priority order
    for i, pattern in enumerate(quiz_patterns):
        try:
            quiz_matches = re.findall(pattern, full_text, re.MULTILINE | re.DOTALL)
            
            if quiz_matches:
                logger.info(f"Using quiz pattern {i+1}, found {len(quiz_matches)} potential matches")
                
                for match in quiz_matches:
                    # Apply smart cleaning cho từng component
                    question_text = text_cleaner.clean_text(match[0])
                    option_a = text_cleaner.clean_text(match[1])
                    option_b = text_cleaner.clean_text(match[2])
                    option_c = text_cleaner.clean_text(match[3])
                    option_d = text_cleaner.clean_text(match[4])
                    
                    # Smart validation
                    if (is_valid_question(question_text) and 
                        all(is_valid_option(opt) for opt in [option_a, option_b, option_c, option_d])):
                        
                        quiz_item = {
                            "question": question_text,
                            "answer": "A",  # placeholder
                            "options": [
                                f"A. {option_a}",
                                f"B. {option_b}",
                                f"C. {option_c}",
                                f"D. {option_d}"
                            ],
                            "type": "quiz_specialized"
                        }
                        quizzes.append(quiz_item)
                
                # Success với pattern này, không thử pattern khác
                if quizzes:
                    logger.info(f"Successfully parsed {len(quizzes)} valid quizzes with pattern {i+1}")
                    break
                    
        except Exception as e:
            logger.warning(f"Error with pattern {i+1}: {e}")
            continue
    
    # Fallback parsing nếu tất cả patterns thất bại
    if not quizzes:
        quizzes = parse_quiz_fallback(full_text)
    
    return quizzes

def parse_quiz_fallback(full_text: str) -> List[Dict[str, Any]]:
    """Enhanced fallback parsing với smart validation"""
    quizzes = []
    
    # Pre-clean full text
    full_text = text_cleaner.remove_unwanted_sections(full_text)
    
    # Split by common question indicators
    question_separators = [
        r'(?=Câu\s*\d+)',
        r'(?=Question\s*\d+)',  
        r'(?=\d+\.)',
        r'(?=\n[^\s\n].*?[?.])'
    ]
    
    blocks = [full_text]  # Start with full text
    
    # Try each separator
    for separator in question_separators:
        new_blocks = []
        for block in blocks:
            new_blocks.extend(re.split(separator, block))
        blocks = new_blocks
        if len(blocks) > 1:  # Found some splits
            break
    
    logger.info(f"Fallback parsing: processing {len(blocks)} text blocks")
    
    for block_idx, block in enumerate(blocks):
        if not block.strip() or len(block.strip()) < 50:
            continue
            
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        
        question = None
        current_options = {'A': None, 'B': None, 'C': None, 'D': None}
        
        # State machine for parsing
        parsing_question = True
        question_lines = []
        
        for line in lines:
            # Skip obvious noise
            if len(line) < 3 or line.lower() in ['a', 'b', 'c', 'd']:
                continue
            
            # Check if this is an option line
            option_match = re.match(r'^([ABCD])\.\s*(.+)', line)
            if option_match:
                parsing_question = False
                option_letter = option_match.group(1)
                option_text = text_cleaner.clean_text(option_match.group(2))
                
                if is_valid_option(option_text):
                    current_options[option_letter] = option_text
                continue
            
            # If we're still parsing question and haven't found all options
            if parsing_question and not all(current_options.values()):
                # Clean and check if this could be part of question
                cleaned_line = text_cleaner.clean_text(line)
                if len(cleaned_line) > 10:
                    question_lines.append(cleaned_line)
        
        # Combine question lines
        if question_lines:
            question = ' '.join(question_lines)
            question = text_cleaner.clean_text(question)
        
        # Validate and create quiz item
        if (question and is_valid_question(question) and 
            all(current_options.values()) and 
            all(is_valid_option(opt) for opt in current_options.values())):
            
            quiz_item = {
                "question": question,
                "answer": "A",  # placeholder
                "options": [
                    f"A. {current_options['A']}",
                    f"B. {current_options['B']}",
                    f"C. {current_options['C']}",
                    f"D. {current_options['D']}"
                ],
                "type": "quiz_specialized"
            }
            quizzes.append(quiz_item)
            logger.info(f"Fallback parsed quiz from block {block_idx}: {question[:50]}...")
    
    return quizzes

def crawl_single_url(url: str) -> List[Dict[str, Any]]:
    """Crawl một URL duy nhất - dành cho threading"""
    thread_name = threading.current_thread().name
    logger.info(f"[{thread_name}] Crawling {url}")
    
    try:
        # Random delay để tránh bị block
        delay = random.uniform(1.0, 3.0)
        time.sleep(delay)
        
        html = fetch_html(url)
        quizzes = parse_quiz(html)
        
        # Nếu không tìm thấy quiz trực tiếp, thử tìm sub-links
        if not quizzes:
            logger.info(f"[{thread_name}] No direct quizzes found, looking for sub-links in {url}")
            sub_links = extract_sub_links(html, url)
            
            if sub_links:
                logger.info(f"[{thread_name}] Found {len(sub_links)} sub-links, crawling them...")
                
                # Crawl từng sub-link (giới hạn 10 link đầu tiên để tránh quá tải)
                for sub_url in sub_links[:10]:
                    try:
                        time.sleep(random.uniform(0.5, 1.0))  # Delay ngắn hơn cho sub-links
                        sub_html = fetch_html(sub_url)
                        sub_quizzes = parse_quiz(sub_html)
                        quizzes.extend(sub_quizzes)
                        
                        if sub_quizzes:
                            logger.info(f"[{thread_name}] Found {len(sub_quizzes)} quizzes from {sub_url}")
                            
                    except Exception as e:
                        logger.warning(f"[{thread_name}] Error crawling sub-link {sub_url}: {e}")
                        continue
        
        logger.info(f"[{thread_name}] Total found {len(quizzes)} quizzes from {url}")
        return quizzes
        
    except Exception as e:
        logger.error(f"[{thread_name}] Error crawling {url}: {e}")
        return []

def load_or_create_dataset(dataset_name: str):
    """Load dataset từ local JSON file hoặc Hugging Face"""
    local_file = f"{dataset_name}.json"
    
    # Ưu tiên load từ file local trước
    if os.path.exists(local_file):
        logger.info(f"Loading existing dataset from local file: {local_file}")
        try:
            with open(local_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Dataset.from_list(data)
        except Exception as e:
            logger.warning(f"Error loading local dataset: {e}, creating new one")
    
    # Nếu không có file local, thử load từ HF
    if HF_TOKEN:
        try:
            logger.info(f"Trying to load dataset from Hugging Face: {dataset_name}")
            ds = load_dataset(dataset_name)
            return ds['train'] if 'train' in ds else ds
        except Exception as e:
            logger.info(f"Could not load from HF: {e}, creating new dataset")
    
    # Tạo dataset mới nếu không load được từ đâu
    logger.info("Creating new empty dataset")
    return Dataset.from_list([])

def merge_datasets(old_ds: Dataset, new_data: List[Dict[str, Any]], strategy="smart_merge"):
    """Merge datasets với các strategy khác nhau"""
    logger.info(f"Merging datasets: old={len(old_ds)}, new={len(new_data)}, strategy={strategy}")
    
    new_ds = Dataset.from_list(new_data)
    
    if strategy == "replace":
        logger.info("Using replace strategy - replacing old dataset")
        return new_ds
    elif strategy == "append":
        logger.info("Using append strategy - appending all new data")
        return concatenate_datasets([old_ds, new_ds])
    elif strategy == "smart_merge":
        # tránh duplicate bằng hash question
        existing_questions = set(old_ds['question']) if len(old_ds) > 0 else set()
        logger.info(f"Found {len(existing_questions)} existing questions")
        
        filtered = [x for x in new_data if x['question'] not in existing_questions]
        logger.info(f"After deduplication: {len(filtered)} new unique questions")
        
        if len(filtered) > 0:
            final_ds = concatenate_datasets([old_ds, Dataset.from_list(filtered)])
        else:
            logger.info("No new unique questions found, keeping original dataset")
            final_ds = old_ds
        
        logger.info(f"Final dataset size: {len(final_ds)}")
        return final_ds
    else:
        raise ValueError(f"Unknown merge strategy: {strategy}")

# --------------------------
# 3. PUSH FUNCTION
# --------------------------
def save_dataset_json(data: List[Dict[str, Any]], filename: str):
    """Lưu dataset dưới dạng JSON array theo format yêu cầu - Thread-safe"""
    with data_lock:  # Ensure thread-safe file writing
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=0, separators=(',', ':'))
        logger.info(f"Saved dataset locally: {filename}")

def push_to_hf(dataset: Dataset, repo_name: str):
    """Push dataset lên Hugging Face - Thread-safe"""
    if not HF_TOKEN:
        logger.warning("HF_TOKEN not set in environment")
        return
    
    try:
        with data_lock:  # Ensure thread-safe HF operations
            create_repo(repo_id=repo_name, repo_type="dataset", exist_ok=True)
            dataset.push_to_hub(repo_name, token=HF_TOKEN)
            logger.info(f"Pushed dataset to Hugging Face: {repo_name}")
    except Exception as e:
        logger.error(f"Error pushing to HF: {e}")

# --------------------------
# INTERACTIVE MENU
# --------------------------
def display_menu():
    """Hiển thị menu lựa chọn merge strategy"""
    print("\n" + "="*60)
    print("🚀 QUIZ CRAWLER - Dataset Merge Options")
    print("="*60)
    print()
    print("Chọn cách xử lý dữ liệu mới với dataset hiện có:")
    print()
    print("1. 📝 APPEND - Thêm tất cả dữ liệu mới (có thể trùng lặp)")
    print("   └── Tốc độ: Nhanh | An toàn: Cao | Dung lượng: Lớn")
    print()
    print("2. 🧠 SMART_MERGE - Chỉ thêm câu hỏi mới (tránh trùng lặp)")
    print("   └── Tốc độ: Trung bình | An toàn: Cao | Dung lượng: Tối ưu")
    print("   └── ⭐ KHUYẾN NGHỊ cho hầu hết trường hợp")
    print()
    print("3. 🔄 REPLACE - Thay thế hoàn toàn dataset cũ")
    print("   └── Tốc độ: Nhanh | An toàn: Thấp | Dung lượng: Nhỏ")
    print("   └── ⚠️  CẢNH BÁO: Sẽ mất tất cả dữ liệu cũ!")
    print()
    print("="*60)

def get_user_choice():
    """Lấy lựa chọn từ người dùng"""
    while True:
        try:
            display_menu()
            choice = input("Nhập lựa chọn của bạn (1/2/3) [mặc định: 2]: ").strip()
            
            # Default choice
            if not choice:
                choice = "2"
            
            if choice == "1":
                strategy = "append"
                print(f"\n✅ Bạn đã chọn: APPEND")
                print("📋 Tất cả dữ liệu mới sẽ được thêm vào dataset hiện có")
                break
            elif choice == "2":
                strategy = "smart_merge"
                print(f"\n✅ Bạn đã chọn: SMART_MERGE")
                print("🧠 Chỉ những câu hỏi mới sẽ được thêm vào (tránh trùng lặp)")
                break
            elif choice == "3":
                strategy = "replace"
                print(f"\n⚠️  Bạn đã chọn: REPLACE")
                confirm = input("🔴 CẢNH BÁO: Điều này sẽ XÓA tất cả dữ liệu cũ! Tiếp tục? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y', 'có']:
                    print("💥 Dataset cũ sẽ bị thay thế hoàn toàn")
                    break
                else:
                    print("🔙 Hủy bỏ, vui lòng chọn lại")
                    continue
            else:
                print("❌ Lựa chọn không hợp lệ! Vui lòng nhập 1, 2 hoặc 3")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Đã hủy bỏ thao tác")
            exit(0)
        except Exception as e:
            print(f"❌ Lỗi: {e}. Vui lòng thử lại")
            continue
    
    return strategy

def show_dataset_info(dataset_name: str):
    """Hiển thị thông tin dataset hiện có"""
    local_file = f"{dataset_name}.json"
    
    print("\n" + "="*50)
    print("📊 THÔNG TIN DATASET HIỆN TẠI")
    print("="*50)
    
    if os.path.exists(local_file):
        try:
            with open(local_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"📁 File: {local_file}")
            print(f"📝 Số câu hỏi hiện có: {len(data)}")
            print(f"💾 Kích thước file: {os.path.getsize(local_file) / 1024:.1f} KB")
            
            # Hiển thị 1 câu hỏi mẫu nếu có
            if len(data) > 0:
                sample = data[0]
                print(f"🔍 Câu hỏi mẫu: {sample.get('question', 'N/A')[:80]}...")
                
        except Exception as e:
            print(f"❌ Không thể đọc file dataset: {e}")
            print("📝 Sẽ tạo dataset mới")
    else:
        print("📝 Chưa có dataset local, sẽ tạo mới")
    
    print("="*50)

# --------------------------
# 4. MAIN WORKFLOW  
# --------------------------
def main(urls: List[str], dataset_name="quiz_dataset", merge_strategy=None, max_workers=MAX_WORKERS):
    """Main workflow với multithreading"""
    
    # Hiển thị thông tin dataset hiện có
    show_dataset_info(dataset_name)
    
    # Nếu không có merge_strategy, hỏi người dùng
    if merge_strategy is None:
        merge_strategy = get_user_choice()
    
    # Xác nhận bắt đầu crawl
    print(f"\n🚀 Bắt đầu crawl {len(urls)} URLs với {max_workers} threads...")
    print(f"📋 Merge strategy: {merge_strategy.upper()}")
    
    try:
        confirm = input("\n▶️  Nhấn Enter để bắt đầu (hoặc Ctrl+C để hủy): ")
    except KeyboardInterrupt:
        print("\n👋 Đã hủy bỏ thao tác")
        return
    
    logger.info(f"Starting crawl with {max_workers} workers for {len(urls)} URLs")
    logger.info(f"Using merge strategy: {merge_strategy}")
    
    all_quizzes = []
    successful_urls = 0
    failed_urls = 0
    
    # Sử dụng ThreadPoolExecutor để crawl đồng thời
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tất cả các URL để crawl
        future_to_url = {executor.submit(crawl_single_url, url): url for url in urls}
        
        # Collect results khi các task hoàn thành
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                quizzes = future.result()
                if quizzes:
                    # Thread-safe append
                    with data_lock:
                        all_quizzes.extend(quizzes)
                    successful_urls += 1
                    print(f"✅ [{successful_urls}/{len(urls)}] Crawled: {len(quizzes)} questions from {url[:50]}...")
                else:
                    failed_urls += 1
                    print(f"⚠️  [{successful_urls + failed_urls}/{len(urls)}] No data from {url[:50]}...")
                    
            except Exception as e:
                failed_urls += 1
                logger.error(f"Exception for {url}: {e}")
                print(f"❌ [{successful_urls + failed_urls}/{len(urls)}] Error: {url[:50]}...")

    print(f"\n📊 Kết quả crawl:")
    print(f"✅ Thành công: {successful_urls} URLs")
    print(f"❌ Thất bại: {failed_urls} URLs") 
    print(f"📝 Tổng câu hỏi mới: {len(all_quizzes)}")

    if not all_quizzes:
        print("⚠️  Không tìm thấy câu hỏi nào!")
        print("💡 Gợi ý: Website có thể có cấu trúc khác, cần cải tiến parsing logic")
        return

    # Load existing dataset và merge (single-threaded operations)
    print(f"\n🔄 Đang xử lý dataset...")
    ds = load_or_create_dataset(dataset_name)
    ds = merge_datasets(ds, all_quizzes, strategy=merge_strategy)
    
    # Convert về list để lưu JSON
    dataset_list = ds.to_list()
    print(f"📊 Kích thước dataset cuối cùng: {len(dataset_list)} câu hỏi")
    
    # Lưu local dưới dạng JSON array
    save_dataset_json(dataset_list, f"{dataset_name}.json")
    
    # Push lên Hugging Face nếu có token
    if HF_TOKEN and HF_REPO:
        print(f"☁️  Đang upload lên Hugging Face...")
        push_to_hf(ds, HF_REPO)
    else:
        print("ℹ️  Bỏ qua upload Hugging Face (không có token hoặc repo)")
    
    print(f"\n🎉 Hoàn thành! Dataset đã được lưu tại: {dataset_name}.json")

def main_batch(urls: List[str], batch_size=50, **kwargs):
    """Xử lý URLs theo batch để tránh quá tải memory"""
    total_batches = (len(urls) + batch_size - 1) // batch_size
    
    print(f"\n📦 Batch Processing Mode")
    print(f"📋 Tổng số URLs: {len(urls)}")
    print(f"📊 Số batch: {total_batches} (mỗi batch {batch_size} URLs)")
    
    # Lấy merge strategy một lần cho tất cả batch
    if 'merge_strategy' not in kwargs or kwargs['merge_strategy'] is None:
        kwargs['merge_strategy'] = get_user_choice()
    
    logger.info(f"Processing {len(urls)} URLs in {total_batches} batches of {batch_size}")
    
    for i in range(0, len(urls), batch_size):
        batch_urls = urls[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        
        print(f"\n🔄 Đang xử lý batch {batch_num}/{total_batches}")
        logger.info(f"Processing batch {batch_num}/{total_batches}")
        
        # Tạo dataset name cho batch này
        batch_dataset_name = f"{kwargs.get('dataset_name', 'quiz_dataset')}_batch_{batch_num}"
        
        # Process batch
        main(batch_urls, dataset_name=batch_dataset_name, **kwargs)
        
        # Optional: delay between batches
        if i + batch_size < len(urls):
            print(f"⏳ Nghỉ 2 giây trước batch tiếp theo...")
            time.sleep(2)

# --------------------------
# 5. ENTRYPOINT
# --------------------------
if __name__ == "__main__":
    # Hiển thị banner
    print("\n" + "="*60)
    print("🕷️  QUIZ CRAWLER - Multithreaded Web Scraper")
    print("="*60)
    
    json_path = "create_dataset/src/vietjack/urls.json"  # đường dẫn tới file JSON chứa các link
    
    if not os.path.exists(json_path):
        print(f"❌ Không tìm thấy file: {json_path}")
        print("📝 Vui lòng tạo file JSON chứa danh sách URLs")
        exit(1)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Lỗi đọc file JSON: {e}")
        exit(1)

    urls_to_crawl = data.get("urls", [])
    if not urls_to_crawl:
        print("❌ File JSON không có key 'urls' hoặc danh sách rỗng")
        exit(1)

    print(f"📋 Đã tải {len(urls_to_crawl)} URLs từ {json_path}")
    
    # Cấu hình từ môi trường
    print(f"⚙️  Cấu hình:")
    print(f"   🧵 Max workers: {MAX_WORKERS}")
    print(f"   ☁️  HF Token: {'✅ Có' if HF_TOKEN else '❌ Không'}")
    print(f"   📦 HF Repo: {HF_REPO if HF_REPO else '❌ Không'}")

    # Chọn mode xử lý
    if len(urls_to_crawl) > 100:
        print(f"\n📦 Phát hiện số lượng URL lớn ({len(urls_to_crawl)}), khuyến nghị dùng batch processing")
        mode_choice = input("Chọn mode: (1) Normal (2) Batch [mặc định: 2]: ").strip()
        
        if mode_choice == "1":
            print("🚀 Chạy mode Normal")
            main(urls_to_crawl, max_workers=MAX_WORKERS)
        else:
            print("📦 Chạy mode Batch Processing")
            batch_size = input("Nhập batch size [mặc định: 50]: ").strip()
            batch_size = int(batch_size) if batch_size.isdigit() else 50
            main_batch(urls_to_crawl, batch_size=batch_size, max_workers=MAX_WORKERS)
    else:
        print("🚀 Chạy mode Normal")
        #main(urls_to_crawl, max_workers=MAX_WORKERS), '', text)
        # Crawl dữ liệu trước
        texts = main(urls_to_crawl, max_workers=MAX_WORKERS)  # trả về list[str]

        # Clean từng text
        cleaned_texts = []
        for text in texts:
            text = re.sub(r'^Câu\s*\d+\s*:\s*', '', text)  # bỏ "Câu X:"
            text = re.sub(r'[“„”‘‚’]', '"', text)         # normalize quotes
            text = re.sub(r'[–—―]', '-', text)             # normalize dashes
            text = re.sub(r'^[:.,-]+\s*', '', text)       # loại bỏ punctuation đầu
            text = re.sub(r'\s*[:.,-]{2,}\s*', ' ', text) # loại bỏ punctuation lặp
            text = re.sub(r'\s+', ' ', text).strip()      # chuẩn hóa spacing
            cleaned_texts.append(text)
        
        
    # Final whitespace cleanup
    def clean_text(text):
        # Normalize quotes và dashes
        text = re.sub(r'[“„”‘‚’]', '"', text)
        text = re.sub(r'[–—―]', '-', text)

        # Clean punctuation
        text = re.sub(r'^[:.,-]+\s*', '', text)
        text = re.sub(r'\s*[:.,-]{2,}\s*', ' ', text)

        # Remove prefix "Câu X:"
        text = re.sub(r'^Câu\s*\d+\s*:\s*', '', text)

        # Final whitespace cleanup
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()

        return text  # ✅ Bên trong function

    def clean_text(self, text: str) -> str:
        """Multi-layer pipeline để clean text"""
        if not text:
            return ""
        
        # Apply all layers sequentially
        text = self.normalize_text(text)
        text = self.remove_unwanted_sections(text)
        text = self.final_cleanup(text)
        
        return text

# Global instance
text_cleaner = SmartTextCleaner()

def clean_text(text: str) -> str:
    """Wrapper function cho backward compatibility"""
    return text_cleaner.clean_text(text)

def is_valid_question(question: str) -> bool:
    """Wrapper function cho question validation"""
    return text_cleaner.is_valid_question(question)

def is_valid_option(option: str) -> bool:
    """Wrapper function cho option validation"""
    return text_cleaner.is_valid_option(option)

def hash_text(text: str) -> str:
    """Tạo unique id từ text"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def fetch_html(url: str) -> str:
    """Thread-safe fetch HTML"""
    scraper = make_scraper()  # Mỗi thread có scraper riêng
    try:
        res = scraper.get(url, timeout=60)
        res.raise_for_status()
        res.encoding = 'utf-8'
        return res.text
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        raise

def extract_sub_links(html: str, base_url: str) -> List[str]:
    """Trích xuất các link con từ trang chính"""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    
    # Tìm tất cả các link có chứa "trac-nghiem" hoặc "bai-hoc"
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Kiểm tra nếu link có chứa trắc nghiệm
        if any(keyword in href.lower() for keyword in ['trac-nghiem', 'bai-hoc', 'quiz']):
            # Tạo absolute URL
            full_url = urljoin(base_url, href)
            
            # Loại bỏ các link không mong muốn
            if not any(unwanted in full_url.lower() for unwanted in ['#', 'javascript:', 'mailto:']):
                links.append(full_url)
    
    # Loại bỏ duplicate
    return list(set(links))

def parse_quiz(html: str) -> List[Dict[str, Any]]:
    """Parse quiz từ HTML - cải tiến để xử lý nhiều format khác nhau"""
    soup = BeautifulSoup(html, "html.parser")

    # Xóa script, style, comment
    for el in soup(['script', 'style']):
        el.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    quizzes = []
    full_text = soup.get_text("\n", strip=False)
    
    # Loại bỏ các section không mong muốn từ full_text trước khi parse
    unwanted_sections = [
        r'Hiển thị đáp án.*?(?=Câu|\n\n|$)',
        r'Show answer.*?(?=Question|\n\n|$)',
        r'Xem đáp án.*?(?=Câu|\n\n|$)',
        r'Đáp án:.*?(?=Câu|\n\n|$)',
        r'Answer:.*?(?=Question|\n\n|$)',
        r'Trắc nghiệm.*?\(có đáp án\).*?(?=Câu|\n\n|$)',
    ]
    
    for pattern in unwanted_sections:
        full_text = re.sub(pattern, '', full_text, flags=re.IGNORECASE | re.MULTILINE)
    
    # Thử nhiều patterns khác nhau
    quiz_patterns = [
        # Pattern 1: Câu hỏi với số thứ tự
        r'(?:Câu\s*\d+\s*[:.]\s*(?:\*\*)?)?(.+?)\n(?=A\.|A\.)\s*A\.\s*(.+?)\n\s*B\.\s*(.+?)\n\s*C\.\s*(.+?)\n\s*D\.\s*(.+?)(?=\nCâu|\n\n|$)',
        
        # Pattern 2: Không có "Câu" prefix
        r'(.+?)\n(?=A\.|A\.)\s*A\.\s*(.+?)\n\s*B\.\s*(.+?)\n\s*C\.\s*(.+?)\n\s*D\.\s*(.+?)(?=\n\w+\.|\n\n|$)',
        
        # Pattern 3: Format đơn giản hơn  
        r'([^\n]+?)\s*\n\s*A\.\s*([^\n]+)\s*\n\s*B\.\s*([^\n]+)\s*\n\s*C\.\s*([^\n]+)\s*\n\s*D\.\s*([^\n]+)',
    ]
    
    # Thử từng pattern
    for i, pattern in enumerate(quiz_patterns):
        quiz_matches = re.findall(pattern, full_text, re.MULTILINE | re.DOTALL)
        
        if quiz_matches:
            logger.info(f"Using quiz pattern {i+1}, found {len(quiz_matches)} potential matches")
            
            for match in quiz_matches:
                question_text = clean_text(match[0])
                option_a = clean_text(match[1])
                option_b = clean_text(match[2])
                option_c = clean_text(match[3])
                option_d = clean_text(match[4])
                
                # Validation nghiêm ngặt
                if (len(question_text) > 15 and 
                    all(len(opt) > 3 for opt in [option_a, option_b, option_c, option_d]) and
                    not any(unwanted.lower() in question_text.lower() for unwanted in 
                           ['hiển thị', 'xem đáp án', 'click', 'bấm'])):
                    
                    quiz_item = {
                        "question": question_text,
                        "answer": "A",  # placeholder
                        "options": [
                            f"A. {option_a}",
                            f"B. {option_b}",
                            f"C. {option_c}",
                            f"D. {option_d}"
                        ],
                        "type": "quiz_specialized"
                    }
                    quizzes.append(quiz_item)
            
            # Nếu tìm thấy quiz với pattern này thì dừng
            if quizzes:
                break
    
    # Fallback parsing nếu tất cả patterns đều thất bại
    if not quizzes:
        quizzes = parse_quiz_fallback(full_text)
    
    return quizzes

def parse_quiz_fallback(full_text: str) -> List[Dict[str, Any]]:
    """Fallback parsing method cho các format khác"""
    quizzes = []
    
    # Split text thành các blocks
    blocks = re.split(r'(?=Câu\s*\d+|Question\s*\d+)', full_text)
    
    for block in blocks:
        if not block.strip():
            continue
            
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        
        question = None
        current_options = {'A': None, 'B': None, 'C': None, 'D': None}
        
        for line in lines:
            # Skip lines with unwanted content
            if any(phrase.lower() in line.lower() for phrase in 
                  ["hiển thị đáp án", "show answer", "xem đáp án", "trắc nghiệm", "(có đáp án)"]):
                continue
                
            # Tìm câu hỏi
            question_match = re.match(r'(?:Câu\s*\d+\s*[:.]\s*(?:\*\*)?)?(.+)', line)
            if question_match and not question and not line.startswith(('A.', 'B.', 'C.', 'D.')):
                potential_question = clean_text(question_match.group(1))
                if len(potential_question) > 15:
                    question = potential_question
                continue
            
            # Tìm các đáp án
            option_match = re.match(r'^([ABCD])\.\s*(.+)', line)
            if option_match:
                option_letter = option_match.group(1)
                option_text = clean_text(option_match.group(2))
                if len(option_text) > 3:
                    current_options[option_letter] = option_text
        
        # Kiểm tra đủ điều kiện tạo quiz
        if question and all(current_options.values()):
            quiz_item = {
                "question": question,
                "answer": "A",  # placeholder
                "options": [
                    f"A. {current_options['A']}",
                    f"B. {current_options['B']}",
                    f"C. {current_options['C']}",
                    f"D. {current_options['D']}"
                ],
                "type": "quiz_specialized"
            }
            quizzes.append(quiz_item)
    
    return quizzes

def crawl_single_url(url: str) -> List[Dict[str, Any]]:
    """Crawl một URL duy nhất - dành cho threading"""
    thread_name = threading.current_thread().name
    logger.info(f"[{thread_name}] Crawling {url}")
    
    try:
        # Random delay để tránh bị block
        delay = random.uniform(1.0, 3.0)
        time.sleep(delay)
        
        html = fetch_html(url)
        quizzes = parse_quiz(html)
        
        # Nếu không tìm thấy quiz trực tiếp, thử tìm sub-links
        if not quizzes:
            logger.info(f"[{thread_name}] No direct quizzes found, looking for sub-links in {url}")
            sub_links = extract_sub_links(html, url)
            
            if sub_links:
                logger.info(f"[{thread_name}] Found {len(sub_links)} sub-links, crawling them...")
                
                # Crawl từng sub-link (giới hạn 10 link đầu tiên để tránh quá tải)
                for sub_url in sub_links[:10]:
                    try:
                        time.sleep(random.uniform(0.5, 1.0))  # Delay ngắn hơn cho sub-links
                        sub_html = fetch_html(sub_url)
                        sub_quizzes = parse_quiz(sub_html)
                        quizzes.extend(sub_quizzes)
                        
                        if sub_quizzes:
                            logger.info(f"[{thread_name}] Found {len(sub_quizzes)} quizzes from {sub_url}")
                            
                    except Exception as e:
                        logger.warning(f"[{thread_name}] Error crawling sub-link {sub_url}: {e}")
                        continue
        
        logger.info(f"[{thread_name}] Total found {len(quizzes)} quizzes from {url}")
        return quizzes
        
    except Exception as e:
        logger.error(f"[{thread_name}] Error crawling {url}: {e}")
        return []

def load_or_create_dataset(dataset_name: str):
    """Load dataset từ local JSON file hoặc Hugging Face"""
    local_file = f"{dataset_name}.json"
    
    # Ưu tiên load từ file local trước
    if os.path.exists(local_file):
        logger.info(f"Loading existing dataset from local file: {local_file}")
        try:
            with open(local_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return Dataset.from_list(data)
        except Exception as e:
            logger.warning(f"Error loading local dataset: {e}, creating new one")
    
    # Nếu không có file local, thử load từ HF
    if HF_TOKEN:
        try:
            logger.info(f"Trying to load dataset from Hugging Face: {dataset_name}")
            ds = load_dataset(dataset_name)
            return ds['train'] if 'train' in ds else ds
        except Exception as e:
            logger.info(f"Could not load from HF: {e}, creating new dataset")
    
    # Tạo dataset mới nếu không load được từ đâu
    logger.info("Creating new empty dataset")
    return Dataset.from_list([])

def merge_datasets(old_ds: Dataset, new_data: List[Dict[str, Any]], strategy="smart_merge"):
    """Merge datasets với các strategy khác nhau"""
    logger.info(f"Merging datasets: old={len(old_ds)}, new={len(new_data)}, strategy={strategy}")
    
    new_ds = Dataset.from_list(new_data)
    
    if strategy == "replace":
        logger.info("Using replace strategy - replacing old dataset")
        return new_ds
    elif strategy == "append":
        logger.info("Using append strategy - appending all new data")
        return concatenate_datasets([old_ds, new_ds])
    elif strategy == "smart_merge":
        # tránh duplicate bằng hash question
        existing_questions = set(old_ds['question']) if len(old_ds) > 0 else set()
        logger.info(f"Found {len(existing_questions)} existing questions")
        
        filtered = [x for x in new_data if x['question'] not in existing_questions]
        logger.info(f"After deduplication: {len(filtered)} new unique questions")
        
        if len(filtered) > 0:
            final_ds = concatenate_datasets([old_ds, Dataset.from_list(filtered)])
        else:
            logger.info("No new unique questions found, keeping original dataset")
            final_ds = old_ds
        
        logger.info(f"Final dataset size: {len(final_ds)}")
        return final_ds
    else:
        raise ValueError(f"Unknown merge strategy: {strategy}")

# --------------------------
# 3. PUSH FUNCTION
# --------------------------
def save_dataset_json(data: List[Dict[str, Any]], filename: str):
    """Lưu dataset dưới dạng JSON array theo format yêu cầu - Thread-safe"""
    with data_lock:  # Ensure thread-safe file writing
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=0, separators=(',', ':'))
        logger.info(f"Saved dataset locally: {filename}")

def push_to_hf(dataset: Dataset, repo_name: str):
    """Push dataset lên Hugging Face - Thread-safe"""
    if not HF_TOKEN:
        logger.warning("HF_TOKEN not set in environment")
        return
    
    try:
        with data_lock:  # Ensure thread-safe HF operations
            create_repo(repo_id=repo_name, repo_type="dataset", exist_ok=True)
            dataset.push_to_hub(repo_name, token=HF_TOKEN)
            logger.info(f"Pushed dataset to Hugging Face: {repo_name}")
    except Exception as e:
        logger.error(f"Error pushing to HF: {e}")

# --------------------------
# INTERACTIVE MENU
# --------------------------
def display_menu():
    """Hiển thị menu lựa chọn merge strategy"""
    print("\n" + "="*60)
    print("🚀 QUIZ CRAWLER - Dataset Merge Options")
    print("="*60)
    print()
    print("Chọn cách xử lý dữ liệu mới với dataset hiện có:")
    print()
    print("1. 📝 APPEND - Thêm tất cả dữ liệu mới (có thể trùng lặp)")
    print("   └── Tốc độ: Nhanh | An toàn: Cao | Dung lượng: Lớn")
    print()
    print("2. 🧠 SMART_MERGE - Chỉ thêm câu hỏi mới (tránh trùng lặp)")
    print("   └── Tốc độ: Trung bình | An toàn: Cao | Dung lượng: Tối ưu")
    print("   └── ⭐ KHUYẾN NGHỊ cho hầu hết trường hợp")
    print()
    print("3. 🔄 REPLACE - Thay thế hoàn toàn dataset cũ")
    print("   └── Tốc độ: Nhanh | An toàn: Thấp | Dung lượng: Nhỏ")
    print("   └── ⚠️  CẢNH BÁO: Sẽ mất tất cả dữ liệu cũ!")
    print()
    print("="*60)

def get_user_choice():
    """Lấy lựa chọn từ người dùng"""
    while True:
        try:
            display_menu()
            choice = input("Nhập lựa chọn của bạn (1/2/3) [mặc định: 2]: ").strip()
            
            # Default choice
            if not choice:
                choice = "2"
            
            if choice == "1":
                strategy = "append"
                print(f"\n✅ Bạn đã chọn: APPEND")
                print("📋 Tất cả dữ liệu mới sẽ được thêm vào dataset hiện có")
                break
            elif choice == "2":
                strategy = "smart_merge"
                print(f"\n✅ Bạn đã chọn: SMART_MERGE")
                print("🧠 Chỉ những câu hỏi mới sẽ được thêm vào (tránh trùng lặp)")
                break
            elif choice == "3":
                strategy = "replace"
                print(f"\n⚠️  Bạn đã chọn: REPLACE")
                confirm = input("🔴 CẢNH BÁO: Điều này sẽ XÓA tất cả dữ liệu cũ! Tiếp tục? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y', 'có']:
                    print("💥 Dataset cũ sẽ bị thay thế hoàn toàn")
                    break
                else:
                    print("🔙 Hủy bỏ, vui lòng chọn lại")
                    continue
            else:
                print("❌ Lựa chọn không hợp lệ! Vui lòng nhập 1, 2 hoặc 3")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Đã hủy bỏ thao tác")
            exit(0)
        except Exception as e:
            print(f"❌ Lỗi: {e}. Vui lòng thử lại")
            continue
    
    return strategy

def show_dataset_info(dataset_name: str):
    """Hiển thị thông tin dataset hiện có"""
    local_file = f"{dataset_name}.json"
    
    print("\n" + "="*50)
    print("📊 THÔNG TIN DATASET HIỆN TẠI")
    print("="*50)
    
    if os.path.exists(local_file):
        try:
            with open(local_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"📁 File: {local_file}")
            print(f"📝 Số câu hỏi hiện có: {len(data)}")
            print(f"💾 Kích thước file: {os.path.getsize(local_file) / 1024:.1f} KB")
            
            # Hiển thị 1 câu hỏi mẫu nếu có
            if len(data) > 0:
                sample = data[0]
                print(f"🔍 Câu hỏi mẫu: {sample.get('question', 'N/A')[:80]}...")
                
        except Exception as e:
            print(f"❌ Không thể đọc file dataset: {e}")
            print("📝 Sẽ tạo dataset mới")
    else:
        print("📝 Chưa có dataset local, sẽ tạo mới")
    
    print("="*50)

# --------------------------
# 4. MAIN WORKFLOW  
# --------------------------
def main(urls: List[str], dataset_name="quiz_dataset", merge_strategy=None, max_workers=MAX_WORKERS):
    """Main workflow với multithreading"""
    
    # Hiển thị thông tin dataset hiện có
    show_dataset_info(dataset_name)
    
    # Nếu không có merge_strategy, hỏi người dùng
    if merge_strategy is None:
        merge_strategy = get_user_choice()
    
    # Xác nhận bắt đầu crawl
    print(f"\n🚀 Bắt đầu crawl {len(urls)} URLs với {max_workers} threads...")
    print(f"📋 Merge strategy: {merge_strategy.upper()}")
    
    try:
        confirm = input("\n▶️  Nhấn Enter để bắt đầu (hoặc Ctrl+C để hủy): ")
    except KeyboardInterrupt:
        print("\n👋 Đã hủy bỏ thao tác")
        return
    
    logger.info(f"Starting crawl with {max_workers} workers for {len(urls)} URLs")
    logger.info(f"Using merge strategy: {merge_strategy}")
    
    all_quizzes = []
    successful_urls = 0
    failed_urls = 0
    
    # Sử dụng ThreadPoolExecutor để crawl đồng thời
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tất cả các URL để crawl
        future_to_url = {executor.submit(crawl_single_url, url): url for url in urls}
        
        # Collect results khi các task hoàn thành
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                quizzes = future.result()
                if quizzes:
                    # Thread-safe append
                    with data_lock:
                        all_quizzes.extend(quizzes)
                    successful_urls += 1
                    print(f"✅ [{successful_urls}/{len(urls)}] Crawled: {len(quizzes)} questions from {url[:50]}...")
                else:
                    failed_urls += 1
                    print(f"⚠️  [{successful_urls + failed_urls}/{len(urls)}] No data from {url[:50]}...")
                    
            except Exception as e:
                failed_urls += 1
                logger.error(f"Exception for {url}: {e}")
                print(f"❌ [{successful_urls + failed_urls}/{len(urls)}] Error: {url[:50]}...")

    print(f"\n📊 Kết quả crawl:")
    print(f"✅ Thành công: {successful_urls} URLs")
    print(f"❌ Thất bại: {failed_urls} URLs") 
    print(f"📝 Tổng câu hỏi mới: {len(all_quizzes)}")

    if not all_quizzes:
        print("⚠️  Không tìm thấy câu hỏi nào!")
        print("💡 Gợi ý: Website có thể có cấu trúc khác, cần cải tiến parsing logic")
        return

    # Load existing dataset và merge (single-threaded operations)
    print(f"\n🔄 Đang xử lý dataset...")
    ds = load_or_create_dataset(dataset_name)
    ds = merge_datasets(ds, all_quizzes, strategy=merge_strategy)
    
    # Convert về list để lưu JSON
    dataset_list = ds.to_list()
    print(f"📊 Kích thước dataset cuối cùng: {len(dataset_list)} câu hỏi")
    
    # Lưu local dưới dạng JSON array
    save_dataset_json(dataset_list, f"{dataset_name}.json")
    
    # Push lên Hugging Face nếu có token
    if HF_TOKEN and HF_REPO:
        print(f"☁️  Đang upload lên Hugging Face...")
        push_to_hf(ds, HF_REPO)
    else:
        print("ℹ️  Bỏ qua upload Hugging Face (không có token hoặc repo)")
    
    print(f"\n🎉 Hoàn thành! Dataset đã được lưu tại: {dataset_name}.json")

def main_batch(urls: List[str], batch_size=50, **kwargs):
    """Xử lý URLs theo batch để tránh quá tải memory"""
    total_batches = (len(urls) + batch_size - 1) // batch_size
    
    print(f"\n📦 Batch Processing Mode")
    print(f"📋 Tổng số URLs: {len(urls)}")
    print(f"📊 Số batch: {total_batches} (mỗi batch {batch_size} URLs)")
    
    # Lấy merge strategy một lần cho tất cả batch
    if 'merge_strategy' not in kwargs or kwargs['merge_strategy'] is None:
        kwargs['merge_strategy'] = get_user_choice()
    
    logger.info(f"Processing {len(urls)} URLs in {total_batches} batches of {batch_size}")
    
    for i in range(0, len(urls), batch_size):
        batch_urls = urls[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        
        print(f"\n🔄 Đang xử lý batch {batch_num}/{total_batches}")
        logger.info(f"Processing batch {batch_num}/{total_batches}")
        
        # Tạo dataset name cho batch này
        batch_dataset_name = f"{kwargs.get('dataset_name', 'quiz_dataset')}_batch_{batch_num}"
        
        # Process batch
        main(batch_urls, dataset_name=batch_dataset_name, **kwargs)
        
        # Optional: delay between batches
        if i + batch_size < len(urls):
            print(f"⏳ Nghỉ 2 giây trước batch tiếp theo...")
            time.sleep(2)

# --------------------------
# 5. ENTRYPOINT
# --------------------------
if __name__ == "__main__":
    # Hiển thị banner
    print("\n" + "="*60)
    print("🕷️  QUIZ CRAWLER - Multithreaded Web Scraper")
    print("="*60)
    
    json_path = "create_dataset/src/vietjack/urls.json"  # đường dẫn tới file JSON chứa các link
    
    if not os.path.exists(json_path):
        print(f"❌ Không tìm thấy file: {json_path}")
        print("📝 Vui lòng tạo file JSON chứa danh sách URLs")
        exit(1)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Lỗi đọc file JSON: {e}")
        exit(1)

    urls_to_crawl = data.get("urls", [])
    if not urls_to_crawl:
        print("❌ File JSON không có key 'urls' hoặc danh sách rỗng")
        exit(1)

    print(f"📋 Đã tải {len(urls_to_crawl)} URLs từ {json_path}")
    
    # Cấu hình từ môi trường
    print(f"⚙️  Cấu hình:")
    print(f"   🧵 Max workers: {MAX_WORKERS}")
    print(f"   ☁️  HF Token: {'✅ Có' if HF_TOKEN else '❌ Không'}")
    print(f"   📦 HF Repo: {HF_REPO if HF_REPO else '❌ Không'}")

    # Chọn mode xử lý
    if len(urls_to_crawl) > 100:
        print(f"\n📦 Phát hiện số lượng URL lớn ({len(urls_to_crawl)}), khuyến nghị dùng batch processing")
        mode_choice = input("Chọn mode: (1) Normal (2) Batch [mặc định: 2]: ").strip()
        
        if mode_choice == "1":
            print("🚀 Chạy mode Normal")
            main(urls_to_crawl, max_workers=MAX_WORKERS)
        else:
            print("📦 Chạy mode Batch Processing")
            batch_size = input("Nhập batch size [mặc định: 50]: ").strip()
            batch_size = int(batch_size) if batch_size.isdigit() else 50
            main_batch(urls_to_crawl, batch_size=batch_size, max_workers=MAX_WORKERS)
    else:
        print("🚀 Chạy mode Normal")
        main(urls_to_crawl, max_workers=MAX_WORKERS)