# ==========================
# Python Full Quiz Crawler
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

# --------------------------
# 2. KHAI BÁO CRAWL FUNCTION
# --------------------------
def make_scraper():
    return cloudscraper.create_scraper(browser={'custom': USER_AGENT})

def clean_text(text: str) -> str:
    """Loại bỏ khoảng trắng thừa, newline, và comment"""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def hash_text(text: str) -> str:
    """Tạo unique id từ text"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def fetch_html(url: str) -> str:
    scraper = make_scraper()
    res = scraper.get(url)
    res.raise_for_status()
    res.encoding = 'utf-8'
    return res.text

def parse_quiz(html: str) -> List[Dict[str, Any]]:
    soup = BeautifulSoup(html, "html.parser")

    # Xóa script, style, comment
    for el in soup(['script', 'style']):
        el.decompose()
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    quizzes = []
    full_text = soup.get_text("\n", strip=False)
    
    # Tìm các câu hỏi dạng "Câu 1: ...", "Q1:", ...
    question_patterns = [
        r"Câu\s*\d+\s*[:.-]\s*(.*?)\n",  # Vietnamese
        r"Q\d+\s*[:.-]\s*(.*?)\n"       # English
    ]
    
    matches = []
    for pattern in question_patterns:
        matches += re.findall(pattern, full_text, re.IGNORECASE | re.DOTALL)
    
    for q in matches:
        cleaned = clean_text(q)
        if cleaned:
            # Định dạng theo yêu cầu
            quiz_item = {
                "question": cleaned,
                "answer": "A",  # placeholder - cần thêm logic parse đáp án thực tế
                "options": [
                    "A. Option A placeholder",
                    "B. Option B placeholder", 
                    "C. Option C placeholder",
                    "D. Option D placeholder"
                ],
                "type": "quiz_specialized"
            }
            quizzes.append(quiz_item)
    
    return quizzes

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
    """Lưu dataset dưới dạng JSON array theo format yêu cầu"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=0, separators=(',', ':'))
    print(f"Saved dataset locally: {filename}")

def push_to_hf(dataset: Dataset, repo_name: str):
    if not HF_TOKEN:
        raise RuntimeError("HF_TOKEN not set in environment")
    
    try:
        create_repo(repo_id=repo_name, repo_type="dataset", exist_ok=True)
        dataset.push_to_hub(repo_name, token=HF_TOKEN)
        print(f"Pushed dataset to Hugging Face: {repo_name}")
    except Exception as e:
        print(f"Error pushing to HF: {e}")

# --------------------------
# 4. MAIN WORKFLOW  
# --------------------------
def main(urls: List[str], dataset_name="quiz_dataset", merge_strategy=MERGE_STRATEGY):
    all_quizzes = []
    
    # Crawl từng URL
    for url in urls:
        print(f"Crawling {url}")
        try:
            html = fetch_html(url)
            quizzes = parse_quiz(html)
            print(f"Found {len(quizzes)} quizzes")
            all_quizzes.extend(quizzes)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
        
        time.sleep(random.uniform(1, 3))  # tránh bị block

    if not all_quizzes:
        print("No quizzes found!")
        return

    # Load existing dataset và merge
    ds = load_or_create_dataset(dataset_name) if HF_TOKEN else Dataset.from_list([])
    ds = merge_datasets(ds, all_quizzes, strategy=merge_strategy)
    
    # Convert về list để lưu JSON
    dataset_list = ds.to_list()
    
    # Lưu local dưới dạng JSON array
    save_dataset_json(dataset_list, f"{dataset_name}.json")
    
    # Push lên Hugging Face nếu có token
    if HF_TOKEN and HF_REPO:
        push_to_hf(ds, HF_REPO)
    else:
        print("HF_TOKEN or HF_REPO not found, skipping Hugging Face upload")

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

    main(urls_to_crawl)