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
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))  # Số luồng tối đa

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

def clean_text(text: str) -> str:
    """Loại bỏ khoảng trắng thừa, newline, comment và các text không mong muốn"""
    if not text:
        return ""
    
    # ==============================================
    # DANH SÁCH CÁC PATTERN NHIỄU DATASET
    # ==============================================
    
    # 1. Tiêu đề bài tập/trắc nghiệm
    title_patterns = [
        r'Trắc nghiệm\s+[^:]*\s*\(có đáp án\)\s*:?\s*',  # "Trắc nghiệm Vật Lí 12 (có đáp án):"
        r'Bài tập\s+[^:]*\s*\(có đáp án\)\s*:?\s*',      # "Bài tập Toán 11 (có đáp án):"
        r'Đề thi\s+[^:]*\s*\(có đáp án\)\s*:?\s*',       # "Đề thi Hóa 10 (có đáp án):"
        r'Kiểm tra\s+[^:]*\s*\(có đáp án\)\s*:?\s*',     # "Kiểm tra Sinh 12 (có đáp án):"
        r'Ôn tập\s+[^:]*\s*\(có đáp án\)\s*:?\s*',       # "Ôn tập Lí 11 (có đáp án):"
        r'Chuyên đề\s+[^:]*\s*\(có đáp án\)\s*:?\s*',    # "Chuyên đề Toán (có đáp án):"
    ]
    
    # 2. Thông tin môn học và lớp
    subject_patterns = [
        r'Trắc nghiệm\s+(Vật\s*Lí|Toán|Hóa|Sinh|Văn|Anh)\s*\d{1,2}\s*',  # "Trắc nghiệm Vật Lí 12"
        r'Bài\s+\d+\s*[:.]\s*',                          # "Bài 8:", "Bài 10:"
        r'Chương\s+\d+\s*[:.]\s*',                       # "Chương 3:"
        r'Phần\s+\d+\s*[:.]\s*',                         # "Phần 2:"
        r'Kết nối tri thức\s*',                          # "Kết nối tri thức"
        r'Chân trời sáng tạo\s*',                        # "Chân trời sáng tạo"
        r'Cánh diều\s*',                                 # "Cánh diều"
    ]
    
    # 3. Thông tin về đáp án và giải thích
    answer_patterns = [
        r'Hiển thị đáp án\s*',
        r'Show answer\s*',
        r'Xem đáp án\s*',
        r'View answer\s*',
        r'Click để xem đáp án\s*',
        r'Bấm để xem đáp án\s*',
        r'Đáp án\s*:\s*[A-D]?\s*',
        r'Answer\s*:\s*[A-D]?\s*',
        r'Giải thích\s*:\s*',
        r'Explanation\s*:\s*',
        r'Lời giải\s*:\s*',
        r'Solution\s*:\s*',
        r'Hướng dẫn giải\s*:\s*',
    ]
    
    # 4. Thông tin về lựa chọn và điều hướng
    navigation_patterns = [
        r'Chọn\s+[A-D]\s+Câu\s+\d+\s*:\s*',            # "Chọn B Câu 6:"
        r'Câu\s+trước\s*',
        r'Câu\s+sau\s*',
        r'Previous\s*',
        r'Next\s*',
        r'Trang\s+\d+\s*',
        r'Page\s+\d+\s*',
    ]
    
    # 5. Metadata và thông tin kỹ thuật
    metadata_patterns = [
        r'\(có đáp án\)\s*:?\s*',                        # "(có đáp án):"
        r'\(with answer\)\s*:?\s*',                      # "(with answer):"
        r'ID\s*:\s*\s*\d+\s*',                             # "ID: 123"
        r'Mã đề\s*:\s*\w+\s*',                          # "Mã đề: AB123"
        r'Thời gian\s*:\s*\d+\s*phút\s*',               # "Thời gian: 45 phút"
        r'Ngày\s*:\s*\d{1,2}/\d{1,2}/\d{4}\s*',        # "Ngày: 15/10/2023"
        r'Tác giả\s*:\s*[^:]+\s*',                       # "Tác giả: Nguyễn A"
    ]
    
    # 6. Thông tin đánh giá và phân loại
    evaluation_patterns = [
        r'Độ khó\s*:\s*[^:]+\s*',                        # "Độ khó: Trung bình"
        r'Mức độ\s*:\s*[^:]+\s*',                        # "Mức độ: Nhận biết"
        r'Điểm\s*:\s*\d+(\.\d+)?\s*',                    # "Điểm: 1.5"
        r'Loại\s*:\s*[^:]+\s*',                          # "Loại: Trắc nghiệm"
        r'Phân loại\s*:\s*[^:]+\s*',                     # "Phân loại: Cơ bản"
    ]
    
    # 7. Số thứ tự và ký hiệu không cần thiết
    numbering_patterns = [
        r'^\d+\.\s*',                                    # "1. " ở đầu câu
        r'^[A-D]\)\s*',                                  # "A) " ở đầu câu  
        r'^\*+\s*',                                      # "*** " ở đầu câu
        r'^#+\s*',                                       # "### " ở đầu câu
        r'^\-+\s*',                                      # "--- " ở đầu câu
    ]
    
    # ==============================================
    # ÁP DỤNG CÁC PATTERN ĐỂ CLEAN TEXT
    # ==============================================
    
    # Gộp tất cả patterns
    all_patterns = (title_patterns + subject_patterns + answer_patterns + 
                   navigation_patterns + metadata_patterns + evaluation_patterns)
    
    # Áp dụng từng pattern (case insensitive)
    for pattern in all_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.MULTILINE)
    
    # Áp dụng numbering patterns (chỉ ở đầu dòng)
    for pattern in numbering_patterns:
        text = re.sub(pattern, '', text, flags=re.MULTILINE)
    
    # Clean up formatting
    text = re.sub(r'[*]{2,}', '', text)        # Remove ** markdown
    text = re.sub(r'_{2,}', '', text)          # Remove __ markdown
    text = re.sub(r'#+', '', text)             # Remove # headers
    text = re.sub(r'\s+', ' ', text)           # Multiple spaces to single
    text = re.sub(r'\n+', ' ', text)           # Multiple newlines to space
    
    # Clean up punctuation
    text = re.sub(r'^[:.,-]+\s*', '', text)    # Remove leading punctuation
    text = re.sub(r'\s*[:.,-]{2,}', '', text)  # Remove multiple consecutive punctuation
    
    # Final cleanup
    text = text.strip()
    
    # Remove very short or meaningless text
    if len(text) < 10 or text.isdigit() or not any(c.isalpha() for c in text):
        return ""
    
    return text

def is_valid_question(question: str) -> bool:
    """Kiểm tra xem câu hỏi có hợp lệ không"""
    if not question or len(question.strip()) < 15:
        return False
    
    # Blacklist các pattern không phải câu hỏi
    invalid_patterns = [
        r'^(Chọn|Choose)\s+[A-D]\s*',                  # "Chọn B"
        r'^(Đáp án|Answer)\s*:?\s*[A-D]\s*',           # "Đáp án: B"
        r'^[A-D]\s*',                                  # "A "
        r'^\d+\s*',                                    # "1 "
        r'^Trang|Page)\s+\d+\s*',                      # "Trang 5"
        r'^(Bài|Lesson)\s+\d+\s*',                     # "Bài 3"
        r'^\W+',                                       # Chỉ có ký tự đặc biệt
    ]
    
    for pattern in invalid_patterns:
        if re.match(pattern, question.strip(), re.IGNORECASE):
            return False
    
    # Câu hỏi hợp lệ phải có ít nhất 3 từ
    words = question.split()
    if len(words) < 3:
        return False
    
    return True

def is_valid_option(option: str) -> bool:
    """Kiểm tra xem đáp án có hợp lệ không"""
    if not option or len(option.strip()) < 3:
        return False
    
    # Loại bỏ các option không hợp lệ
    invalid_option_patterns = [
        r'^(Xem|View|See)\s+(đáp án|answer)',          # "Xem đáp án"
        r'^(Click|Bấm|Nhấn)',                          # "Click để xem"
        r'^\W+',                                       # Chỉ có ký tự đặc biệt
        r'^\d+\s*',                                    # Chỉ là số
        r'^[A-D]\s*',                                  # Chỉ là chữ cái
    ]
    
    for pattern in invalid_option_patterns:
        if re.match(pattern, option.strip(), re.IGNORECASE):
            return False
    
    return True

def crawl_single_url(url: str) -> List[Dict[str, Any]]:
    """Crawl một URL duy nhất - dành cho threading"""
    thread_name = threading.current_thread().name
    logger.info(f"[{thread_name}] Crawling {url}")
    
    try:
        # Random delay để tránh bị block
        delay = random.uniform(0.5, 2.0)
        time.sleep(delay)
        
        html = fetch_html(url)
        quizzes = parse_quiz(html)
        
        logger.info(f"[{thread_name}] Found {len(quizzes)} quizzes from {url}")
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
    
    json_path = "create_dataset/src/tech12/urls.json"  # đường dẫn tới file JSON chứa các link
    
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