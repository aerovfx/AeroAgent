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
    """Loại bỏ khoảng trắng thừa, newline, và comment"""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def hash_text(text: str) -> str:
    """Tạo unique id từ text"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def fetch_html(url: str) -> str:
    """Thread-safe fetch HTML"""
    scraper = make_scraper()  # Mỗi thread có scraper riêng
    try:
        res = scraper.get(url, timeout=30)
        res.raise_for_status()
        res.encoding = 'utf-8'
        return res.text
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        raise

def parse_quiz(html: str) -> List[Dict[str, Any]]:
    """Parse quiz từ HTML - thread-safe"""
    soup = BeautifulSoup(html, "html.parser")

    # Xóa script, style, comment
    for el in soup(['script', 'style']):
        el.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    quizzes = []
    full_text = soup.get_text("\n", strip=False)
    
    # Pattern tìm câu hỏi và các đáp án
    # Sử dụng regex để capture cả câu hỏi và các đáp án
    quiz_pattern = r'(?:Câu\s*\d+\s*[:.]\s*\*\*)?(.+?)\n(?=A\.|A\.)\s*A\.\s*(.+?)\n\s*B\.\s*(.+?)\n\s*C\.\s*(.+?)\n\s*D\.\s*(.+?)(?=\n|$)'
    
    # Tìm các quiz blocks
    quiz_matches = re.findall(quiz_pattern, full_text, re.MULTILINE | re.DOTALL)
    
    for match in quiz_matches:
        question_text = clean_text(match[0])
        option_a = clean_text(match[1])
        option_b = clean_text(match[2])
        option_c = clean_text(match[3])
        option_d = clean_text(match[4])
        
        if question_text and all([option_a, option_b, option_c, option_d]):
            quiz_item = {
                "question": question_text,
                "answer": "A",  # placeholder - có thể thêm logic để detect đáp án đúng
                "options": [
                    f"A. {option_a}",
                    f"B. {option_b}",
                    f"C. {option_c}",
                    f"D. {option_d}"
                ],
                "type": "quiz_specialized"
            }
            quizzes.append(quiz_item)
    
    # Fallback: nếu không tìm thấy với pattern trên, dùng pattern cũ
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
        options = []
        current_options = {'A': None, 'B': None, 'C': None, 'D': None}
        
        for line in lines:
            # Tìm câu hỏi
            question_match = re.match(r'(?:Câu\s*\d+\s*[:.]\s*(?:\*\*)?)?(.+)', line)
            if question_match and not question and not line.startswith(('A.', 'B.', 'C.', 'D.')):
                question = clean_text(question_match.group(1))
                continue
            
            # Tìm các đáp án
            option_match = re.match(r'^([ABCD])\.\s*(.+)', line)
            if option_match:
                option_letter = option_match.group(1)
                option_text = clean_text(option_match.group(2))
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
    try:
        ds = load_dataset(dataset_name)
        return ds
    except:
        return Dataset.from_list([])

def merge_datasets(old_ds: Dataset, new_data: List[Dict[str, Any]], strategy="smart_merge"):
    new_ds = Dataset.from_list(new_data)
    if strategy == "replace":
        return new_ds
    elif strategy == "append":
        return concatenate_datasets([old_ds, new_ds])
    elif strategy == "smart_merge":
        # tránh duplicate bằng hash question
        existing_questions = set(old_ds['question']) if len(old_ds) > 0 else set()
        filtered = [x for x in new_data if x['question'] not in existing_questions]
        return concatenate_datasets([old_ds, Dataset.from_list(filtered)])
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
# 4. MAIN WORKFLOW  
# --------------------------
def main(urls: List[str], dataset_name="quiz_dataset", merge_strategy=MERGE_STRATEGY, max_workers=MAX_WORKERS):
    """Main workflow với multithreading"""
    logger.info(f"Starting crawl with {max_workers} workers for {len(urls)} URLs")
    
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
                else:
                    failed_urls += 1
                    
            except Exception as e:
                logger.error(f"Exception for {url}: {e}")
                failed_urls += 1

    logger.info(f"Crawl completed: {successful_urls} successful, {failed_urls} failed")
    logger.info(f"Total quizzes found: {len(all_quizzes)}")

    if not all_quizzes:
        logger.warning("No quizzes found!")
        return

    # Load existing dataset và merge (single-threaded operations)
    logger.info("Processing dataset...")
    ds = load_or_create_dataset(dataset_name) if HF_TOKEN else Dataset.from_list([])
    ds = merge_datasets(ds, all_quizzes, strategy=merge_strategy)
    
    # Convert về list để lưu JSON
    dataset_list = ds.to_list()
    logger.info(f"Final dataset size: {len(dataset_list)} items")
    
    # Lưu local dưới dạng JSON array
    save_dataset_json(dataset_list, f"{dataset_name}.json")
    
    # Push lên Hugging Face nếu có token
    if HF_TOKEN and HF_REPO:
        logger.info("Pushing to Hugging Face...")
        push_to_hf(ds, HF_REPO)
    else:
        logger.warning("HF_TOKEN or HF_REPO not found, skipping Hugging Face upload")

def main_batch(urls: List[str], batch_size=50, **kwargs):
    """Xử lý URLs theo batch để tránh quá tải memory"""
    total_batches = (len(urls) + batch_size - 1) // batch_size
    logger.info(f"Processing {len(urls)} URLs in {total_batches} batches of {batch_size}")
    
    all_results = []
    
    for i in range(0, len(urls), batch_size):
        batch_urls = urls[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        
        logger.info(f"Processing batch {batch_num}/{total_batches}")
        
        # Tạo dataset name cho batch này
        batch_dataset_name = f"{kwargs.get('dataset_name', 'quiz_dataset')}_batch_{batch_num}"
        
        # Process batch
        main(batch_urls, dataset_name=batch_dataset_name, **kwargs)
        
        # Optional: delay between batches
        if i + batch_size < len(urls):
            time.sleep(2)

# --------------------------
# 5. ENTRYPOINT
# --------------------------
if __name__ == "__main__":
    json_path = "create_dataset/src/tech12/urls.json"  # đường dẫn tới file JSON chứa các link
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Không tìm thấy file: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls_to_crawl = data.get("urls", [])
    if not urls_to_crawl:
        raise ValueError("File JSON không có key 'urls' hoặc rỗng")

    # Có thể dùng main() cho crawl bình thường hoặc main_batch() cho số lượng URL lớn
    if len(urls_to_crawl) > 100:
        logger.info("Large number of URLs detected, using batch processing")
        main_batch(urls_to_crawl, batch_size=50, max_workers=MAX_WORKERS)
    else:
        main(urls_to_crawl, max_workers=MAX_WORKERS)