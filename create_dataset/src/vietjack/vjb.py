#!/usr/bin/env python3
# coding: utf-8

import os
import re
import json
import time
import random
import hashlib
import logging
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from urllib.parse import urljoin, urlparse

import requests
import cloudscraper
from bs4 import BeautifulSoup, Comment

# Optional HF
try:
    from datasets import Dataset
    from huggingface_hub import create_repo
    HF_AVAILABLE = True
except Exception:
    HF_AVAILABLE = False

from dotenv import load_dotenv

# ---------------------------
# Config / .env
# ---------------------------
# load .env located two levels above this script (create_dataset/.env)
dotenv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", ".env")
)
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    # try project root .env
    load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_REPO = os.getenv("HF_REPO")
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "6"))

# Save files to same folder as script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("quiz-crawler")

# Thread-safe
data_lock = Lock()

# ---------------------------
# Utilities: Fetch HTML
# ---------------------------
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
}

def fetch_html(url: str, timeout: int = 20, retry: int = 3) -> str:
    """Fetch HTML with requests and fallback to cloudscraper when needed."""
    for attempt in range(retry):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200 and len(r.text) > 200:
                r.encoding = r.apparent_encoding or "utf-8"
                return r.text
            # fallback
            scraper = cloudscraper.create_scraper()
            r = scraper.get(url, headers=HEADERS, timeout=timeout)
            if r.status_code == 200:
                r.encoding = r.apparent_encoding or "utf-8"
                return r.text
        except Exception as e:
            logger.debug(f"fetch_html attempt {attempt+1} failed for {url}: {e}")
            time.sleep(1 + attempt)
    logger.warning(f"fetch_html failed for {url}")
    return ""

# ---------------------------
# Link extraction
# ---------------------------
def get_sub_links(category_url: str, keep_part: str = "trac-nghiem") -> List[str]:
    """Extract sub-links from category page that contain keep_part and same domain"""
    html = fetch_html(category_url)
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")

    base = "{uri.scheme}://{uri.netloc}".format(uri=urlparse(category_url))
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("#") or href.lower().startswith("javascript:") or href.startswith("mailto:"):
            continue
        full = urljoin(category_url, href)
        # filter: same domain and contain keep_part
        if full.startswith(base) and keep_part in full.lower():
            # ignore image/pdf/resource links
            if any(full.lower().endswith(ext) for ext in [".jpg", ".png", ".gif", ".pdf", ".zip"]):
                continue
            if full not in links:
                links.append(full)
    logger.info(f"Found {len(links)} sub-links in category {category_url}")
    return links

# ---------------------------
# Cleaning & validation
# ---------------------------
UNWANTED_PHRASES = [
    "hiển thị đáp án", "xem đáp án", "show answer", "click để xem đáp án",
    "đáp án:", "answer:", "giải thích:", "explanation:", "lời giải:", "solution:"
]

def clean_text(text: str) -> str:
    if not text:
        return ""
    s = text.strip()
    # remove common unwanted phrases
    for p in UNWANTED_PHRASES:
        s = re.sub(re.escape(p), '', s, flags=re.IGNORECASE)
    # remove extra whitespace and repeated punctuation
    s = re.sub(r'\s+', ' ', s)
    s = s.strip(" \t\n\r:.-–")
    return s.strip()

def is_valid_question(q: str) -> bool:
    if not q:
        return False
    q = q.strip()
    if len(q) < 10:
        return False
    # must contain at least one alphabetic character and a space (multiple words)
    if not any(c.isalpha() for c in q):
        return False
    if len(q.split()) < 3:
        return False
    # blacklist small patterns
    if re.match(r'^(đáp án|answer|hiển thị|xem|show)\b', q, flags=re.IGNORECASE):
        return False
    return True

def is_valid_option(opt: str) -> bool:
    if not opt:
        return False
    opt = opt.strip()
    if len(opt) < 1:
        return False
    if len(opt) < 2:
        return False
    # avoid "Xem đáp án" etc
    if re.search(r'(xem đáp án|hiển thị đáp án|click để xem|bấm để xem|solution|explanation)', opt, flags=re.I):
        return False
    return True

# ---------------------------
# Parsing quiz blocks
# ---------------------------
QUIZ_BLOCK_RE = re.compile(
    r'(Câu\s*\d+\s*[:.)]?\s*.*?)'      # group 1: starts with "Câu N: ..." up to next
    r'(?=(?:\nCâu\s*\d+\s*[:.)]|\Z))',
    flags=re.I | re.S
)

OPTION_LINE_RE = re.compile(r'^[\s]*([A-D])[\.\)]\s*(.+)', flags=re.I)

def parse_quiz_from_html(html: str, source_url: str = "") -> List[Dict[str, Any]]:
    """Parse HTML to extract quiz items. Returns list of dicts."""
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    # remove scripts/styles/comments
    for tag in soup(["script", "style"]):
        tag.decompose()
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()

    text = soup.get_text("\n", strip=True)
    # normalize newlines (some pages have no newlines)
    text = re.sub(r'\r', '\n', text)
    # Remove headers like "Trắc nghiệm ... (có đáp án)" that may sit before first question
    text = re.sub(r'Trắc nghiệm[^\n]{0,120}\(có đáp án\)[^\n]*\n', '', text, flags=re.I)

    items = []

    # Try to find blocks that start with "Câu N"
    blocks = re.split(r'(?=(?:Câu\s*\d+\s*[:.)]))', text, flags=re.I)
    # If split produced empty first part, skip
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # only consider blocks that begin with "Câu"
        if not re.match(r'^Câu\s*\d+', block, flags=re.I):
            continue

        # Extract question line(s) until first option marker A. or A)
        # find first occurrence of option marker
        opt_pos = re.search(r'\n?\s*[A-D][\.\)]\s', block)
        if opt_pos:
            q_part = block[:opt_pos.start()].strip()
            opts_part = block[opt_pos.start():].strip()
        else:
            # fallback: block may have options inline; try to split by " A. "
            if " A. " in block:
                q_part, opts_part = block.split(" A. ", 1)
                opts_part = "A. " + opts_part
            else:
                # no options - skip
                continue

        question = clean_text(re.sub(r'^Câu\s*\d+\s*[:.)]?\s*', '', q_part, flags=re.I))
        if not is_valid_question(question):
            continue

        # parse options lines from opts_part
        opt_lines = re.split(r'\n+', opts_part)
        options = {}
        for line in opt_lines:
            m = OPTION_LINE_RE.match(line.strip())
            if m:
                letter = m.group(1).upper()
                text_opt = clean_text(m.group(2))
                options[letter] = text_opt
            else:
                # some options wrap to following lines; append to last option if present
                if options and line.strip():
                    last = sorted(options.keys())[-1]
                    options[last] = options[last] + " " + clean_text(line.strip())

        # ensure we have at least A-D
        if all(is_valid_option(options.get(ch, "")) for ch in ["A", "B", "C", "D"]):
            item = {
                "question": question,
                "options": [f"A. {options['A']}", f"B. {options['B']}", f"C. {options['C']}", f"D. {options['D']}"],
                "answer": None,   # answer often not present in page text; left None
                "source": source_url,
                "type": "mcq"
            }
            items.append(item)

    # If nothing found via block method, try fallback scanning for patterns A./B./C./D. across whole text
    if not items:
        # find occurrences where A. ... B. ... C. ... D.
        fallback_pattern = re.compile(
            r'(.{20,300}?)\s+(?:A[\.\)]\s*(.+?)\s+B[\.\)]\s*(.+?)\s+C[\.\)]\s*(.+?)\s+D[\.\)]\s*(.+?))(?=\n|$)',
            flags=re.S | re.I
        )
        for m in fallback_pattern.finditer(text):
            question = clean_text(m.group(1))
            a = clean_text(m.group(2)); b = clean_text(m.group(3)); c = clean_text(m.group(4)); d = clean_text(m.group(5))
            if is_valid_question(question) and all(is_valid_option(x) for x in [a,b,c,d]):
                items.append({
                    "question": question,
                    "options": [f"A. {a}", f"B. {b}", f"C. {c}", f"D. {d}"],
                    "answer": None,
                    "source": source_url,
                    "type": "mcq"
                })

    return items

# ---------------------------
# Dedupe & Merge
# ---------------------------
def dedupe_by_question(items: List[Dict[str,Any]]) -> List[Dict[str,Any]]:
    seen = set()
    out = []
    for it in items:
        q = it.get("question","").strip()
        h = hashlib.md5(q.encode("utf-8")).hexdigest()
        if h not in seen:
            seen.add(h)
            out.append(it)
    return out

# ---------------------------
# Save & optional HF push
# ---------------------------
def save_json(items: List[Dict[str,Any]], filename: str):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"quizzes": items}, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved {len(items)} quizzes to {path}")

def push_to_hf_local_file(filename: str, repo_name: str):
    """Upload local file to huggingface dataset repo (simple: upload file only).
       Requires HF_TOKEN and HF_REPO set in .env. This uses huggingface_hub.upload_file."""
    try:
        from huggingface_hub import HfApi
        api = HfApi()
        api.set_access_token(HF_TOKEN)
        # create repo if missing
        try:
            create_repo(repo_id=repo_name, repo_type="dataset", exist_ok=True, token=HF_TOKEN)
        except Exception as e:
            logger.debug(f"create_repo warning: {e}")
        local_path = os.path.join(BASE_DIR, filename)
        # upload to repo root as quizzes.json
        api.upload_file(path_or_fileobj=local_path, path_in_repo=filename, repo_id=repo_name, repo_type="dataset", token=HF_TOKEN)
        logger.info(f"Uploaded {filename} to Hugging Face dataset {repo_name}")
    except Exception as e:
        logger.error(f"Failed to upload to Hugging Face: {e}")

# ---------------------------
# Crawl single page wrapper for ThreadPool
# ---------------------------
def crawl_page(url: str) -> List[Dict[str,Any]]:
    try:
        html = fetch_html(url)
        if not html:
            return []
        quizzes = parse_quiz_from_html(html, source_url=url)
        return quizzes
    except Exception as e:
        logger.error(f"crawl_page error for {url}: {e}")
        return []

# ---------------------------
# Main entrypoint
# ---------------------------
def main_interactive():
    print("=== QUIZ CRAWLER ===")
    category = input("Enter category URL to crawl sub-links (e.g. https://vietjack.com/...): ").strip()
    if not category:
        print("No URL provided. Exit.")
        return

    # get sub links
    sub_links = get_sub_links(category, keep_part="trac-nghiem")
    if not sub_links:
        print("No quiz links found on category page.")
        return

    print(f"Found {len(sub_links)} sub-links. Crawling with {MAX_WORKERS} workers...")

    all_items = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exec:
        futures = {exec.submit(crawl_page, u): u for u in sub_links}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                items = fut.result()
                if items:
                    with data_lock:
                        all_items.extend(items)
                    print(f"[+] {len(items)} quizzes from {url}")
                else:
                    print(f"[-] No quizzes from {url}")
            except Exception as e:
                print(f"[!] Error crawling {url}: {e}")

    # dedupe
    logger.info(f"Total raw quizzes collected: {len(all_items)}")
    deduped = dedupe_by_question(all_items)
    logger.info(f"After dedupe: {len(deduped)}")

    # Save to same folder
    filename = "quiz_dataset.json"
    save_json(deduped, filename)

    # optional push to HF
    if HF_TOKEN and HF_REPO and HF_AVAILABLE:
        push = input("Upload to Hugging Face dataset repo? (y/N): ").strip().lower() == "y"
        if push:
            push_to_hf_local_file(filename, HF_REPO)
    else:
        logger.info("HF upload skipped (missing HF_TOKEN/HF_REPO or `datasets` not installed).")

    print("Done.")

if __name__ == "__main__":
    main_interactive()