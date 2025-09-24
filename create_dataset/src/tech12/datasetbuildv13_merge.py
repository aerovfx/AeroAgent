import os
import json
import time
import random
import requests
from bs4 import BeautifulSoup, NavigableString, Comment
from urllib.parse import urlparse, urljoin
import cloudscraper
import re
from collections import defaultdict
import hashlib
from typing import List, Dict, Any
from datasets import Dataset
from huggingface_hub import login
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Lock cho print để tránh race condition
print_lock = threading.Lock()

# --- Cải tiến tải HTML ---
def fetch_html(url, retry=3):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        ]),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    
    for attempt in range(retry):
        try:
            session = requests.Session()
            resp = session.get(url, headers=headers, timeout=20)
            
            if resp.status_code == 200 and len(resp.text) > 500:
                return resp.text
            else:
                with print_lock:
                    print(f"   ⚠️ Attempt {attempt+1}: Status {resp.status_code}, trying cloudscraper...")
                scraper = cloudscraper.create_scraper()
                resp = scraper.get(url, headers=headers, timeout=20)
                if resp.status_code == 200:
                    return resp.text
        except Exception as e:
            with print_lock:
                print(f"   ❌ Attempt {attempt+1} failed: {e}")
            if attempt < retry - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    
    return None

# --- Kiểm tra trang có phải trắc nghiệm không (CẢI TIẾN: Thêm patterns, tối ưu scoring) ---
def is_quiz_page(soup, url):
    """
    Kiểm tra nghiêm ngặt xem trang có phải là trắc nghiệm không
    - Thêm patterns mới cho quiz
    - Tăng trọng số cho structure
    - Giảm threshold cho strong evidence
    """
    # Kiểm tra URL patterns (mạnh nhất)
    quiz_url_patterns = [
        'trac-nghiem', 'quiz', 'test', 'kiem-tra', 'de-thi', 
        'bai-kiem-tra', 'bai-tap-trac-nghiem', 'multiple-choice',
        'mcq', 'examination', 'on-tap', 'luyen-tap', 'bai-tap', 'cau-hoi'
    ]
    
    url_lower = url.lower()
    has_quiz_url = any(pattern in url_lower for pattern in quiz_url_patterns)
    
    # Kiểm tra title và meta description
    title = soup.select_one('title')
    title_text = title.get_text().lower() if title else ""
    
    meta_desc = soup.select_one('meta[name="description"]')
    meta_desc_text = meta_desc.get('content', '').lower() if meta_desc else ""
    
    quiz_title_patterns = [
        'trắc nghiệm', 'quiz', 'test', 'câu hỏi trắc nghiệm',
        'bài kiểm tra', 'đề thi', 'multiple choice', 'ôn tập', 'luyện thi'
    ]
    
    has_quiz_title = any(pattern in title_text or pattern in meta_desc_text 
                        for pattern in quiz_title_patterns)
    
    # Kiểm tra nội dung trang (patterns mạnh - CẢI TIẾN: Thêm patterns)
    page_text = soup.get_text().lower()
    
    # Patterns mạnh cho trắc nghiệm
    strong_quiz_patterns = [
        r'câu\s+\d+[.:\s]+',  # Câu 1:, Câu 2.
        r'question\s+\d+[.:\s]+',  # Question 1:
        r'[abcd][\.\)]\s+[^\n]{10,}',  # A. something, B) something
        r'chọn\s+đáp\s+án\s+đúng',  # chọn đáp án đúng
        r'đáp\s+án\s+đúng\s+là',  # đáp án đúng là
        r'lựa\s+chọn\s+đúng',  # lựa chọn đúng
        r'đáp án\s*[abcd]',  # đáp án A
        r'correct answer',  # correct answer
        r'select the correct',  # select the correct
        r'multiple choice'  # multiple choice
    ]
    
    strong_quiz_matches = sum(len(re.findall(pattern, page_text, re.IGNORECASE)) 
                             for pattern in strong_quiz_patterns)
    
    # Kiểm tra cấu trúc HTML (forms, inputs radio/checkbox - CẢI TIẾN: Thêm selectors)
    quiz_forms = soup.select('form[class*="quiz"], form[id*="quiz"], form[class*="test"], div[class*="quiz"], div[class*="test"]')
    radio_inputs = soup.select('input[type="radio"]')
    checkbox_inputs = soup.select('input[type="checkbox"]')
    
    has_quiz_structure = len(quiz_forms) > 0 or len(radio_inputs) >= 3 or len(checkbox_inputs) >= 3  # Giảm từ 4 xuống 3
    
    # Scoring system (CẢI TIẾN: Tối ưu weights)
    score = 0
    if has_quiz_url:
        score += 4  # Tăng trọng số cho URL
    if has_quiz_title:
        score += 3  # Tăng cho title
    if strong_quiz_matches >= 3:  # Giảm threshold từ 5 xuống 3
        score += 4
    if has_quiz_structure:
        score += 3  # Tăng cho structure
    
    # Kiểm tra negative indicators (loại trừ)
    negative_patterns = [
        'giới thiệu', 'about', 'contact', 'liên hệ', 'tin tức', 'news',
        'blog', 'bài viết', 'article', 'hướng dẫn', 'tutorial',
        'danh mục', 'category', 'archive', 'trang chủ', 'home'
    ]
    
    has_negative = any(pattern in url_lower or pattern in title_text 
                      for pattern in negative_patterns)
    
    if has_negative:
        score -= 3  # Tăng penalty
    
    is_quiz = score >= 5  # Tăng threshold từ 4 lên 5 để nghiêm ngặt hơn, nhưng với weights mới sẽ dễ pass hơn nếu có evidence mạnh
    
    with print_lock:
        print(f"   🎯 Quiz check: score={score}, is_quiz={is_quiz} - {url}")
    
    return is_quiz

# --- Tìm quiz links với filter nghiêm ngặt (CẢI TIẾN: Thêm patterns, scoring chi tiết) ---
def get_quiz_links_only(url):
    html = fetch_html(url)
    if not html:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    quiz_links = []
    seen_urls = set()
    
    with print_lock:
        print("   🔍 Tìm QUIZ LINKS (filter nghiêm ngặt)...")
    
    for a in soup.find_all("a", href=True):
        href = a.get("href", "").strip()
        if not href:
            continue
            
        full_url = urljoin(url, href)
        
        # Chỉ lấy links trong domain
        if not full_url.startswith("https://tech12h.com") or full_url == url:
            continue
            
        # Skip unwanted patterns
        skip_patterns = [
            '#', 'javascript:', 'mailto:', '.jpg', '.png', '.gif', '.pdf', 
            '.zip', '.rar', 'facebook.com', 'twitter.com', 'youtube.com',
            '/wp-admin', '/wp-content/uploads', '?replytocom=', '?share=',
            '/category/', '/tag/', '/author/', '/page/', '/search/',
            '/contact/', '/about/', '/lien-he/', '/gioi-thieu/'
        ]
        
        if any(pattern in full_url.lower() for pattern in skip_patterns):
            continue
            
        if full_url in seen_urls:
            continue
        seen_urls.add(full_url)
        
        # STRONG QUIZ DETECTION từ link text và URL (CẢI TIẾN: Thêm patterns)
        link_text = a.get_text(strip=True).lower()
        url_lower = full_url.lower()
        
        # Must have patterns (ít nhất 1 trong số này)
        must_have_patterns = [
            'trac-nghiem', 'quiz', 'test', 'kiem-tra', 'de-thi',
            'bai-kiem-tra', 'multiple-choice', 'mcq', 'on-tap',
            'luyen-tap', 'bai-tap-trac-nghiem', 'cau-hoi-trac-nghiem'
        ]
        
        # Link text indicators
        quiz_link_texts = [
            'trắc nghiệm', 'quiz', 'test', 'câu hỏi', 'bài kiểm tra',
            'đề thi', 'ôn tập', 'luyện tập', 'bài tập', 'kiểm tra kiến thức'
        ]
        
        has_must_have = any(pattern in url_lower for pattern in must_have_patterns)
        has_quiz_text = any(pattern in link_text for pattern in quiz_link_texts)
        
        # Scoring for link (CẢI TIẾN: Thêm bonus cho số và môn học)
        link_score = 0
        if has_must_have:
            link_score += 3
        if has_quiz_text:
            link_score += 2
        
        # Bonus if both URL and text indicate quiz
        if has_must_have and has_quiz_text:
            link_score += 1
        
        # Bonus for subject-specific (math, physics, etc.)
        subject_patterns = ['toan', 'ly', 'hoa', 'sinh', 'su', 'dia', 'anh', 'van']
        if any(sub in url_lower or sub in link_text for sub in subject_patterns):
            link_score += 1
        
        # Must meet minimum threshold
        if link_score >= 3:
            quiz_links.append(full_url)
    
    with print_lock:
        print(f"   ✅ Tìm thấy {len(quiz_links)} quiz links tiềm năng")
    
    return quiz_links

# --- Crawl đệ quy chỉ quiz (CẢI TIẾN: Tăng sample_links, thêm visited check chặt hơn) ---
def get_all_quiz_links_recursive(start_url, visited=None, max_depth=2, current_depth=0):
    if visited is None:
        visited = set()
    
    if current_depth > max_depth or start_url in visited:
        return []
    
    visited.add(start_url)
    with print_lock:
        print(f"   🕸️  Quiz crawling depth {current_depth}: {start_url}")
    
    quiz_links = get_quiz_links_only(start_url)
    all_quiz_links = []
    
    # Verify mỗi link có thực sự là quiz không
    for link in quiz_links:
        if link not in visited:
            html = fetch_html(link)
            if html:
                soup = BeautifulSoup(html, "html.parser")
                if is_quiz_page(soup, link):
                    all_quiz_links.append(link)
                    with print_lock:
                        print(f"     ✅ Confirmed quiz: {link}")
                else:
                    with print_lock:
                        print(f"     ❌ False positive: {link}")
    
    # Recurse (limit để tránh deep crawl)
    if current_depth < max_depth:
        sample_links = quiz_links[:10]  # Tăng từ 5 lên 10 để rộng hơn
        for link in sample_links:
            if link not in visited:
                sub_quiz = get_all_quiz_links_recursive(link, visited, max_depth, current_depth + 1)
                all_quiz_links.extend(sub_quiz)
    
    return list(set(all_quiz_links))  # Remove duplicates

# --- Thay thế hình ảnh công thức bằng LaTeX ---
def replace_math_images(element):
    """Thay thế các hình ảnh công thức toán học bằng mã LaTeX từ alt text"""
    math_symbols = ['=', '+', '-', '*', '/', '^', '∫', '∑', '√', 'π', 'θ', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'λ', 'μ', 'ν', 'ξ', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ψ', 'ω']
    for img in element.find_all('img'):
        alt = img.get('alt', '').strip()
        title = img.get('title', '').strip()
        src_lower = img.get('src', '').lower()
        
        # Kiểm tra nếu là hình ảnh công thức (CẢI TIẾN: Thêm check cho src)
        if (('math' in src_lower or 'formula' in src_lower or 'equation' in src_lower or 'latex' in src_lower or
             any(sym in alt for sym in math_symbols) or any(sym in title for sym in math_symbols))):
            
            latex_content = alt if alt else title
            if latex_content:
                latex_content = re.sub(r'(\w+)\^(\d+)', r'\1^{\2}', latex_content)
                latex_content = re.sub(r'(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)', r'\\frac{\1}{\2}', latex_content)
                # Use inline math for quiz
                replacement = NavigableString(f"${latex_content}$")
                img.replace_with(replacement)
    
    return element

# --- Xử lý văn bản để thêm math mode ---
def process_math_content(text):
    """Xử lý văn bản để wrap các phần có thể là công thức vào math mode và fix LaTeX"""
    if not text:
        return text
    
    # First, fix existing LaTeX formatting
    text = fix_latex_formatting(text)
    
    # Find mathematical expressions that aren't already in math mode
    # Pattern for basic math expressions (avoid double-wrapping) (CẢI TIẾN: Mở rộng pattern)
    math_pattern = r'(?<!\$)([a-zA-Z0-9αβγδεζηθλμνξπρστφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]+\s*[+\-*/=^√∫∑<>≤≥≠]+\s*[a-zA-Z0-9αβγδεζηθλμνξπρστφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]+)(?!\$)'
    
    def replace_math(match):
        expr = match.group(1).strip()
        
        # Skip if already contains LaTeX commands
        if '\\' in expr:
            return f'${expr}$'
        
        # Basic LaTeX improvements
        expr = re.sub(r'([a-zA-Z0-9]+)\^([a-zA-Z0-9]+)', r'\1^{\2}', expr)  # a^b -> a^{b}
        expr = re.sub(r'(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)', r'\\frac{\1}{\2}', expr)  # 1/2 -> \frac{1}{2}
        expr = re.sub(r'sqrt\(([^)]+)\)', r'\\sqrt{\1}', expr)  # sqrt(x) -> \sqrt{x}
        
        return f'${expr}$'
    
    # Apply math wrapping only to non-$ expressions
    text = re.sub(math_pattern, replace_math, text)
    
    return text

def fix_latex_formatting(text: str) -> str:
    """Sửa các lỗi LaTeX formatting phổ biến (CẢI TIẾN: Thêm fixes cho Greek và functions)"""
    if not text:
        return ""
    
    # Fix common LaTeX syntax errors from the examples
    
    # 1. Fix sin$\alpha -> sin\alpha (remove $ inside function names)
    text = re.sub(r'(sin|cos|tan|cot|sec|csc|log|ln|exp)\$\\?([a-zA-Zαβγδ]+)', r'\1\2', text, flags=re.IGNORECASE)
    
    # 2. Fix $sin{2}$\alpha -> $sin^2\alpha$
    text = re.sub(r'\$(sin|cos|tan|cot)\{(\d+)\}\$\\([a-zA-Zαβγδ]+)', r'$\1^{ \2 }\3$', text, flags=re.IGNORECASE)
    
    # 3. Fix double $ issues: $$expr$ -> $expr$
    text = re.sub(r'\$\$([^$]+)\$\$', r'$\1$', text)
    
    # 4. Fix $\alpha +1$ -> $\alpha + 1$
    text = re.sub(r'\$([^\$]+?)([+\-*/=])\s*(\d+)\$', r'$\1 \2 \3$', text)
    
    # 5. Fix missing spaces around operators in LaTeX
    text = re.sub(r'\$([^$]*[a-zA-Z])\+([^$]*)\$', r'$\1 + \2$', text)
    text = re.sub(r'\$([^$]*[a-zA-Z])\-([^$]*)\$', r'$\1 - \2$', text)
    text = re.sub(r'\$([^$]*[a-zA-Z])\*([^$]*)\$', r'$\1 \times \2$', text)  # Thêm fix cho *
    
    # 6. Fix \frac syntax: \frac{a}{b} format
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\\frac{\1}{\2}', text)
    
    # 7. Fix function names without backslash
    function_names = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'log', 'ln', 'exp', 'lim', 'max', 'min', 'sqrt']
    for func in function_names:
        # Fix bare function names in math mode
        text = re.sub(rf'\$([^$]*?)({func})([^a-zA-Z])', rf'$\1\\{func}\3', text, flags=re.IGNORECASE)
    
    # 8. Fix sqrt: sqrt{expr} -> \sqrt{expr}
    text = re.sub(r'sqrt\{([^}]+)\}', r'\\sqrt{\1}', text)
    
    # 9. Fix fractions without \frac
    text = re.sub(r'\$([^$]*?)(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)([^$]*?)\$', r'$\1\\frac{\2}{\3}\4$', text)
    
    # 10. Fix Greek letters without backslash
    greek_letters = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 
                     'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'pi', 'rho', 'sigma', 
                     'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
    for letter in greek_letters:
        text = re.sub(rf'\$([^$]*?)({letter})([^a-zA-Z])', rf'$\1\\{letter}\3', text, flags=re.IGNORECASE)
    
    # 11. Fix exponents: a^2 -> a^{2} if not already wrapped
    text = re.sub(r'\$([^$]*?)([a-zA-Z])\^(\d+)([^${]*?)\$', r'$\1\2^{\3}\4$', text)
    
    # 12. Clean up multiple spaces in math mode
    text = re.sub(r'\$([^$]*?)\s{2,}([^$]*?)\$', r'$\1 \2$', text)
    
    # 13. Fix missing $ closure
    # Count $ symbols and add missing one if odd
    dollar_count = text.count('$')
    if dollar_count % 2 == 1:
        text = text + '$'
    
    # Clean up extra spaces around math symbols
    text = re.sub(r'\s*\$\s*', '$', text)
    text = re.sub(r'\s*\\\s*', '\\\\', text)
    
    return text.strip()

# --- Trích xuất trắc nghiệm CHUYÊN BIỆT (CẢI TIẾN: Thêm patterns, cải tiến extraction) ---
def extract_quiz_specialized(soup):
    """
    Trích xuất trắc nghiệm chuyên biệt - CHỈ FOCUS VÀO QUIZ
    - Thêm patterns cho extraction
    - Cải tiến option and answer extraction
    - Thêm fallback cho unstructured text
    """
    questions = []
    
    with print_lock:
        print("   🎯 SPECIALIZED QUIZ EXTRACTION...")
    
    # Áp dụng thay thế math images
    replace_math_images(soup)
    
    # Method 1: Numbered Questions Pattern (CẢI TIẾN: Thêm patterns)
    full_text = soup.get_text(separator='\n', strip=True)
    
    # Enhanced patterns cho câu hỏi trắc nghiệm
    question_patterns = [
        # Vietnamese patterns
        r'Câu\s+(\d+)[.:\s]+(.*?)(?=Câu\s+\d+|$)',
        r'Question\s+(\d+)[.:\s]+(.*?)(?=Question\s+\d+|$)',
        r'(\d+)[.]\s+(.*?)(?=\d+[.]|$)',
        r'(\d+)\)\s+(.*?)(?=\d+\)|$)',
        r'Câu hỏi\s+(\d+)[.:\s]+(.*?)(?=Câu hỏi\s+\d+|$)',  # Thêm
        r'Bài\s+(\d+)[.:\s]+(.*?)(?=Bài\s+\d+|$)'  # Thêm
    ]
    
    pattern_found = False
    for pattern in question_patterns:
        matches = re.findall(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if len(matches) >= 2:  # Giảm từ 3 xuống 2 để linh hoạt hơn
            with print_lock:
                print(f"   📝 Pattern match: {len(matches)} questions found")
            pattern_found = True
            
            for match in matches:
                if isinstance(match, tuple) and len(match) >= 2:
                    q_num, q_content = match[0], match[1]
                    
                    # Clean and process content (remove "Câu X:")
                    q_content = q_content.strip()[:2000]  # Limit length
                    q_content = clean_quiz_text(q_content)  # Remove "Câu X:" first
                    q_content = process_math_content(q_content)  # Then process math
                    
                    # Extract options (A. B. C. D.) (CẢI TIẾN: Mở rộng pattern)
                    options = []
                    option_pattern = r'([ABCD])[.\)]\s*([^\n\r]+?)(?=[ABCD][.\)]|$)'
                    option_matches = re.findall(option_pattern, q_content, re.MULTILINE | re.IGNORECASE)
                    
                    if option_matches:
                        options = []
                        for opt in option_matches:
                            if len(opt) >= 2:
                                opt_text = clean_quiz_text(opt[1].strip())
                                opt_text = process_math_content(opt_text)
                                if len(opt_text) > 3:  # Meaningful option
                                    options.append(f"{opt[0].upper()}. {opt_text}")
                    
                    # Extract answer (CẢI TIẾN: Thêm patterns)
                    answer = None
                    answer_patterns = [
                        r'Đáp\s+án[:\s]*([ABCD])',
                        r'Answer[:\s]*([ABCD])',
                        r'Chọn[:\s]*([ABCD])',
                        r'Correct[:\s]*([ABCD])',
                        r'Đáp án đúng[:\s]*([ABCD])',  # Thêm
                        r'Lựa chọn[:\s]*([ABCD])'  # Thêm
                    ]
                    
                    for ans_pattern in answer_patterns:
                        ans_match = re.search(ans_pattern, q_content, re.IGNORECASE)
                        if ans_match:
                            answer = ans_match.group(1).upper()
                            break
                    
                    # Create clean question text
                    final_question = clean_quiz_text(q_content)
                    final_question = process_math_content(final_question)
                    
                    # Quality check
                    if len(final_question) > 15 and (len(options) >= 2 or answer):
                        questions.append({
                            "question": final_question,
                            "options": options if len(options) >= 2 else None,
                            "answer": answer,
                            "type": "quiz_specialized",
                            "extraction_method": "numbered_pattern"
                        })
            if pattern_found:
                break  # Use first successful pattern
    
    # Method 2: HTML Structure Analysis (QUIZ-FOCUSED) (CẢI TIẾN: Thêm selectors)
    if not questions:  # Only if method 1 failed
        quiz_specific_selectors = [
            'div[class*="quiz"]', 'div[class*="question"]', 'div[class*="mcq"]',
            'form[class*="quiz"]', 'div[class*="test"]', '.quiz-container',
            '.question-container', '.mcq-container', '.test-container',
            'div[class*="trac-nghiem"]', 'section[class*="quiz"]'  # Thêm
        ]
        
        for selector in quiz_specific_selectors:
            containers = soup.select(selector)
            if containers:
                with print_lock:
                    print(f"   🏗️ Using selector: {selector} ({len(containers)} containers)")
                
                for container in containers:
                    replace_math_images(container)
                    text = container.get_text(strip=True)
                    
                    if 30 <= len(text) <= 1500:  # Reasonable question length
                        # Clean text and remove "Câu X:" prefix
                        text = clean_quiz_text(text)
                        text = process_math_content(text)
                        
                        # Extract options from container (CẢI TIẾN: Thêm selectors)
                        options = []
                        option_selectors = [
                            'input[type="radio"] + label',
                            'input[type="checkbox"] + label',
                            '.option', '.choice', '.answer-option',
                            'li[class*="option"]', 'div[class*="choice"]'  # Thêm
                        ]
                        
                        for opt_sel in option_selectors:
                            opt_elements = container.select(opt_sel)
                            if opt_elements:
                                options = []
                                for opt in opt_elements:
                                    opt_text = clean_quiz_text(opt.get_text(strip=True))
                                    opt_text = process_math_content(opt_text)
                                    if len(opt_text) > 3:
                                        options.append(opt_text)
                                break
                        
                        # Extract correct answer (CẢI TIẾN: Thêm selectors)
                        answer = None
                        correct_selectors = [
                            'input[checked] + label', '.correct', '.right-answer',
                            '[data-correct="true"]', '.answer-key',
                            '.dap-an', '[class*="correct"]'  # Thêm
                        ]
                        
                        for ans_sel in correct_selectors:
                            ans_element = container.select_one(ans_sel)
                            if ans_element:
                                answer = clean_quiz_text(ans_element.get_text(strip=True))
                                answer = process_math_content(answer)
                                break
                        
                        questions.append({
                            "question": text,
                            "options": options if len(options) >= 2 else None,
                            "answer": answer,
                            "type": "quiz_specialized",
                            "extraction_method": "html_structure"
                        })
                if questions:
                    break  # Use first successful selector
    
    # Method 3: Table-based Quizzes (CẢI TIẾN: Cải tiến cell handling)
    if not questions:  # Only if previous methods failed
        tables = soup.find_all('table')
        for table in tables:
            replace_math_images(table)
            rows = table.find_all('tr')[1:]  # Skip header
            
            table_questions = []
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    question_cell = cells[0]
                    replace_math_images(question_cell)
                    question_text = question_cell.get_text(strip=True)
                    question_text = clean_quiz_text(question_text)  # Remove "Câu X:"
                    question_text = process_math_content(question_text)
                    
                    # Try to get answer from other cells
                    answer = None
                    if len(cells) > 1:
                        answer_cell = cells[-1]
                        replace_math_images(answer_cell)
                        answer = answer_cell.get_text(strip=True)
                        answer = clean_quiz_text(answer)
                        answer = process_math_content(answer)
                    
                    if len(question_text) > 15:  # Increased minimum length
                        table_questions.append({
                            "question": question_text,
                            "answer": answer,
                            "type": "quiz_specialized",
                            "extraction_method": "table_structure"
                        })
            
            if len(table_questions) >= 2:  # Giảm từ 3 xuống 2
                questions.extend(table_questions)
                break
    
    # Final quality filter
    filtered_questions = []
    for q in questions:
        # Must have meaningful content
        if (len(q["question"]) >= 20 and 
            (q.get("options") or q.get("answer")) and
            not is_low_quality_quiz_content(q["question"])):
            filtered_questions.append(q)
    
    with print_lock:
        print(f"   ✅ Extracted {len(filtered_questions)} high-quality quiz questions")
    
    return filtered_questions

def is_low_quality_quiz_content(text):
    """Kiểm tra nội dung quiz chất lượng thấp (CẢI TIẾN: Thêm indicators)"""
    low_quality_indicators = [
        'click here', 'read more', 'xem thêm', 'đọc tiếp',
        'advertisement', 'quảng cáo', 'facebook', 'twitter',
        'cookie', 'privacy', 'terms', 'điều khoản',
        'giới thiệu', 'about us', 'contact', 'liên hệ',
        'home', 'trang chủ', 'menu', 'navigation'  # Thêm
    ]
    
    text_lower = text.lower()
    return any(indicator in text_lower for indicator in low_quality_indicators)

# --- Scraper chính CHỈ QUIZ ---
def scrape_quiz_only(url, debug=False):
    """
    Scrape CHỈ trắc nghiệm, bỏ qua mọi nội dung khác
    """
    with print_lock:
        print(f"\n🎯 QUIZ-ONLY SCRAPING: {url}")
    
    html = fetch_html(url)
    if not html:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    
    # FIRST: Verify this is actually a quiz page
    if not is_quiz_page(soup, url):
        with print_lock:
            print("   ❌ NOT A QUIZ PAGE - SKIPPING")
        return []
    
    # Debug mode
    if debug:
        debug_quiz_structure(soup, url)
    
    # Extract quiz questions
    questions = extract_quiz_specialized(soup)
    
    # Filter and deduplicate
    questions = filter_and_deduplicate_questions(questions)
    
    with print_lock:
        print(f"   ✅ Final: {len(questions)} quiz questions from this page")
    
    return questions

def debug_quiz_structure(soup, url):
    """Debug cấu trúc quiz page (CẢI TIẾN: Thêm chi tiết)"""
    with print_lock:
        print(f"\n🔬 DEBUGGING QUIZ PAGE: {url}")
        print("-" * 60)
    
    # Check quiz indicators
    quiz_indicators = soup.select('[class*="quiz"], [id*="quiz"], [class*="test"], [class*="question"]')
    with print_lock:
        print(f"🎯 Quiz indicators found: {len(quiz_indicators)}")
    
    # Check form elements
    radio_inputs = soup.select('input[type="radio"]')
    checkbox_inputs = soup.select('input[type="checkbox"]')
    with print_lock:
        print(f"📝 Radio inputs: {len(radio_inputs)}, Checkboxes: {len(checkbox_inputs)}")
    
    # Check common patterns
    full_text = soup.get_text()
    cau_pattern_count = len(re.findall(r'Câu\s+\d+', full_text, re.IGNORECASE))
    option_pattern_count = len(re.findall(r'[ABCD][.\)]\s+', full_text))
    
    with print_lock:
        print(f"🔢 'Câu X' patterns: {cau_pattern_count}")
        print(f"🔤 'A./B./C./D.' patterns: {option_pattern_count}")
        print("-" * 60)

# --- Validation và filtering ---
def filter_and_deduplicate_questions(questions):
    """Lọc và loại bỏ câu hỏi trùng lặp - QUIZ FOCUSED"""
    seen_hashes = set()
    filtered = []
    
    for q in questions:
        # Tạo hash cho content
        content_hash = hashlib.md5(
            (q.get('question', '') + str(q.get('answer', ''))).encode()
        ).hexdigest()
        
        if content_hash not in seen_hashes:
            # Quiz-specific quality check
            if is_high_quality_quiz(q):
                seen_hashes.add(content_hash)
                filtered.append(q)
    
    return filtered

def is_high_quality_quiz(q):
    """Kiểm tra chất lượng cao của câu hỏi trắc nghiệm (CẢI TIẾN: Nới lỏng length)"""
    question = q.get('question', '')
    options = q.get('options', [])
    answer = q.get('answer', '')
    
    # Length checks
    if not (15 <= len(question) <= 1000):  # Giảm từ 20 xuống 15
        return False
    
    # Must have answer OR options
    if not options and not answer:
        return False
    
    # If has options, must be reasonable number
    if options and not (2 <= len(options) <= 6):
        return False
    
    # Content quality
    if is_low_quality_quiz_content(question):
        return False
    
    # Quiz-specific patterns (bonus points)
    quiz_question_patterns = [
        r'[?]',  # Has question mark
        r'Câu\s+\d+',  # Numbered question
        r'[ABCD][.\)]',  # Has options
        r'chọn|lựa chọn|đúng|sai',  # Choice keywords
    ]
    
    pattern_score = sum(1 for pattern in quiz_question_patterns 
                       if re.search(pattern, question, re.IGNORECASE))
    
    return pattern_score >= 1  # Must match at least 1 quiz pattern

# --- Main execution CHỈ QUIZ ---
def run_quiz_only_scraper():
    print("🎯 QUIZ-ONLY CRAWLER - Specialized for Multiple Choice Questions")
    print("📚 Only crawls and extracts quiz/test content, ignoring everything else")
    print("-" * 70)
    
    parent_url = input("Nhập URL cần scrape quiz (mặc định https://tech12h.com): ").strip()
    if not parent_url:
        parent_url = "https://tech12h.com"
    
    debug_mode = input("Debug mode? (y/N): ").strip().lower() == 'y'
    max_depth = input("Độ sâu crawl quiz (mặc định 2): ").strip()
    max_depth = int(max_depth) if max_depth.isdigit() else 2
    
    repo_name = input("Nhập tên repo Hugging Face (e.g., username/quiz-dataset): ").strip()
    if not repo_name:
        print("Tên repo không hợp lệ! Thoát.")
        return
    
    hf_token = input("Nhập Hugging Face token (optional): ").strip()
    
    max_workers = input("Số threads song song (mặc định 3): ").strip()
    max_workers = int(max_workers) if max_workers.isdigit() else 3
    
    print(f"\n🔍 Starting QUIZ-ONLY analysis: {parent_url}")
    
    # Phase 1: Get all quiz links
    print("\n📦 Phase 1: Discovering quiz pages...")
    quiz_links = get_all_quiz_links_recursive(parent_url, max_depth=max_depth)
    
    if not quiz_links:
        print("⚠️ No quiz pages found! Checking main URL...")
        html = fetch_html(parent_url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            if is_quiz_page(soup, parent_url):
                quiz_links = [parent_url]
            else:
                print("❌ Main URL is not a quiz page either!")
                return
    
    print(f"✅ Found {len(quiz_links)} confirmed quiz pages")
    
    # Phase 2: Extract quiz questions
    print(f"\n📝 Phase 2: Extracting quiz questions (threads={max_workers})...")
    
    all_questions = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {
            executor.submit(scrape_quiz_only, link, debug_mode and i == 0): link 
            for i, link in enumerate(quiz_links)
        }
        
        for future in as_completed(future_to_url):
            link = future_to_url[future]
            try:
                questions_from_page = future.result()
                if questions_from_page:
                    all_questions.extend(questions_from_page)
                    with print_lock:
                        print(f"   ✅ {len(questions_from_page)} questions from {link}")
                else:
                    with print_lock:
                        print(f"   ⚠️ No quiz content from {link}")
            except Exception as e:
                with print_lock:
                    print(f"   ❌ Error scraping {link}: {e}")
            
            # Rate limiting
            time.sleep(random.uniform(0.5, 1.0))
    
    print(f"\n✅ Total quiz questions extracted: {len(all_questions)}")
    
    if not all_questions:
        print("❌ No quiz questions found!")
        return
    
    # Phase 3: Normalize and validate
    print("\n🔧 Phase 3: Normalizing and validating quiz questions...")
    
    normalized_questions = []
    for q in all_questions:
        norm_q = normalize_quiz_question(q)
        if norm_q:
            normalized_questions.append(norm_q)
    
    print(f"✅ Normalized: {len(normalized_questions)} questions")
    
    validated_questions = validate_quiz_questions(normalized_questions)
    print(f"✅ Validated: {len(validated_questions)} high-quality quiz questions")
    
    if not validated_questions:
        print("❌ No valid quiz questions after validation!")
        return
    
    # Phase 4: Create dataset
    print("\n📄 Phase 4: Creating JSONL dataset...")
    jsonl_file = create_jsonl(validated_questions, "quiz_dataset.jsonl")
    
    # Phase 5: Push to Hugging Face
    print("\n🚀 Phase 5: Pushing to Hugging Face...")
    
    merge_strategy = input("Chọn merge strategy (append/smart_merge/replace) [append]: ").strip()
    if not merge_strategy:
        merge_strategy = "append"
    
    try:
        # Comment out if dataset_merger not available; fallback to simple push
        # from dataset_merger import push_to_huggingface_with_merge
        # hf_url = push_to_huggingface_with_merge(jsonl_file, repo_name, hf_token, merge_strategy)
        # print(f"✅ Successfully merged and pushed to: {hf_url}")
        
        # Fallback to simple push
        push_to_huggingface(jsonl_file, repo_name, hf_token if hf_token else None)
        print("✅ Successfully pushed to Hugging Face!")
        print(f"💡 For merge strategies, use the separate dataset_merger.py module")
        
    except Exception as e:
        print(f"❌ Failed to push to Hugging Face: {e}")
    
    # Final Summary
    print("\n" + "="*70)
    print("🎯 QUIZ-ONLY SCRAPER SUMMARY")
    print("="*70)
    print(f"📊 Quiz pages discovered: {len(quiz_links)}")
    print(f"📝 Total questions extracted: {len(all_questions)}")
    print(f"✅ Valid quiz questions: {len(validated_questions)}")
    print(f"📁 Dataset file: {jsonl_file}")
    print(f"🌐 HF Repository: https://huggingface.co/datasets/{repo_name}")
    
    # Question type breakdown
    type_counts = {}
    for q in validated_questions:
        q_type = q.get('type', 'unknown')
        type_counts[q_type] = type_counts.get(q_type, 0) + 1
    
    print(f"\n📈 Question Type Breakdown:")
    for q_type, count in type_counts.items():
        print(f"   {q_type}: {count} questions")
    
    print("="*70)

# --- Normalize quiz question ---
def normalize_quiz_question(q: Dict[str, Any]) -> Dict[str, Any]:
    """Chuẩn hóa câu hỏi trắc nghiệm"""
    if not q.get("question"):
        return None
    
    normalized = {
        "question": str(q.get("question", "")).strip(),
        "answer": str(q.get("answer", "")).strip() if q.get("answer") else None,
        "options": q.get("options", None),
        "type": q.get("type", "quiz"),
        "extraction_method": q.get("extraction_method", "unknown")
    }
    
    # Clean question
    normalized["question"] = clean_quiz_text(normalized["question"])
    
    # Clean answer
    if normalized["answer"]:
        normalized["answer"] = clean_quiz_text(normalized["answer"])
    
    # Clean options
    if normalized["options"] and isinstance(normalized["options"], list):
        cleaned_options = []
        for opt in normalized["options"]:
            clean_opt = clean_quiz_text(str(opt))
            if clean_opt and len(clean_opt) > 2:
                cleaned_options.append(clean_opt)
        normalized["options"] = cleaned_options if len(cleaned_options) >= 2 else None
    
    return normalized if normalized["question"] else None

def clean_quiz_text(text: str) -> str:
    """Làm sạch text cho quiz và loại bỏ 'Câu X:' (CẢI TIẾN: Mở rộng removal patterns)"""
    if not text:
        return ""
    
    # 1. Remove "Câu X:" patterns at the beginning
    text = re.sub(r'^(Câu|Question|Câu hỏi|Bài|Question No)\s*\d+\s*[:\.\)]\s*', '', text.strip(), flags=re.IGNORECASE)
    
    # 2. Fix LaTeX formatting issues
    text = fix_latex_formatting(text)
    
    # 3. Remove multiple whitespaces
    text = re.sub(r'\s+', ' ', text.strip())
    
    # 4. Remove unwanted characters but keep Vietnamese, math symbols, and LaTeX
    keep_chars = r'[\w\s\.,\?!:;\(\)\[\]\{\}+\-*/=<>∑∫√π θ α β γ δ ε ζ η λ μ ν ξ ρ σ τ φ χ ψ ω Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω ° % à á ạ ả ã â ầ ấ ậ ẩ ẫ ă ằ ắ ặ ẳ ẵ è é ẹ ẻ ẽ ê ề ế ệ ể ễ ì í ị ỉ ĩ ò ó ọ ỏ õ ô ồ ố ộ ổ ỗ ơ ờ ớ ợ ở ỡ ù ú ụ ủ ũ ư ừ ứ ự ử ữ ỳ ý ỵ ỷ ỹ đ À Á Ạ Ả Ã Â Ầ Ấ Ậ Ẩ Ẫ Ă Ằ Ắ Ặ Ẳ Ẵ È É Ẹ Ẻ Ẽ Ê Ề Ế Ệ Ể Ễ Ì Í Ị Ỉ Ĩ Ò Ó Ọ Ỏ Õ Ô Ồ Ố Ộ Ổ Ỗ Ơ Ờ Ớ Ợ Ở ỡ Ù Ú Ụ Ủ Ũ Ư Ừ Ứ Ự Ử Ữ Ỳ Ý Ỵ Ỷ Ỹ Đ \\ $ ^ _ { } \']'
    text = re.sub(f'[^ {keep_chars}]', '', text)
    
    # 5. Fix common OCR errors in Vietnamese
    text = text.replace('đ ề', 'đề').replace('c â u', 'câu').replace('d á p', 'đáp')
    
    # 6. Clean up extra spaces around math symbols
    text = re.sub(r'\s*\$\s*', '$', text)
    text = re.sub(r'\s*\\\s*', '\\\\', text)
    
    return text.strip()

# --- Validate quiz questions ---
def validate_quiz_questions(questions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate quiz questions với các rule nghiêm ngặt"""
    valid_questions = []
    
    for q in questions:
        if validate_single_quiz(q):
            valid_questions.append(q)
    
    with print_lock:
        print(f"   ✅ Quiz validation: {len(valid_questions)} valid out of {len(questions)}")
    
    return valid_questions

def validate_single_quiz(q: Dict[str, Any]) -> bool:
    """Validate một câu hỏi quiz (CẢI TIẾN: Thêm indicators)"""
    # Must have question
    question = q.get("question", "")
    if not question or len(question) < 15:
        return False
    
    # Must have answer OR options
    answer = q.get("answer")
    options = q.get("options")
    
    if not answer and not options:
        return False
    
    # If has options, must be reasonable
    if options:
        if not isinstance(options, list) or len(options) < 2:
            return False
        
        # Each option must be meaningful
        valid_options = [opt for opt in options if len(str(opt).strip()) > 2]
        if len(valid_options) < 2:
            return False
    
    # Quiz-specific validation
    question_lower = question.lower()
    
    # Must have quiz indicators (CẢI TIẾN: Thêm)
    quiz_indicators = [
        'câu', 'question', 'chọn', 'choose', 'đúng', 'correct',
        'sai', 'wrong', 'a.', 'b.', 'c.', 'd.', 'a)', 'b)', 'c)', 'd)',
        'lựa chọn', 'đáp án', 'multiple'  # Thêm
    ]
    
    has_indicator = any(indicator in question_lower for indicator in quiz_indicators)
    
    # Must not have non-quiz indicators
    non_quiz_indicators = [
        'giới thiệu', 'introduction', 'tóm tắt', 'summary',
        'liên hệ', 'contact', 'about', 'home page'
    ]
    
    has_non_quiz = any(indicator in question_lower for indicator in non_quiz_indicators)
    
    return has_indicator and not has_non_quiz

# --- Create JSONL ---
def create_jsonl(questions: List[Dict[str, Any]], output_file: str = "quiz_dataset.jsonl"):
    """Tạo file JSONL từ quiz questions"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for q in questions:
            f.write(json.dumps(q, ensure_ascii=False) + '\n')
    
    with print_lock:
        print(f"📄 Created JSONL file: {output_file} ({len(questions)} questions)")
    return output_file

# --- Push to Hugging Face ---
def push_to_huggingface(jsonl_file: str, repo_name: str, hf_token: str = None):
    """Push quiz dataset to Hugging Face Hub"""
    if hf_token:
        login(token=hf_token)
    
    # Load dataset
    dataset = Dataset.from_json(jsonl_file)
    
    # Add metadata
    dataset_info = {
        "description": "Vietnamese Quiz/Multiple Choice Questions Dataset",
        "language": "vi",
        "task": "question-answering",
        "domain": "education",
        "source": "tech12h.com",
        "extraction_method": "specialized_quiz_crawler"
    }
    
    # Push to hub
    dataset.push_to_hub(repo_name, private=False)
    
    with print_lock:
        print(f"🚀 Successfully pushed to: https://huggingface.co/datasets/{repo_name}")

# --- Test function cho text cleaning ---
def test_text_cleaning():
    """Test function để demo việc làm sạch text"""
    test_cases = [
        "Câu 3: Kết quả rút gọn của biểu thức $(\frac{sin\$alpha + tan$\alpha }{cos\$alpha +1$})$2+1$ bằng: A. $\frac{1}{$sin{2}$\alpha }$ B. 2 C. 1 + $tan\alpha$ D. $\frac{1}{$cos{2}$\alpha }$",
        "Câu 6: Cho cosα = 0,2 vơi 0 < α π. A. cos$\frac{α}{2}$ = $\frac{\sqrt{3}}{\sqrt{5}}$ B. sin$\frac{α}{2}$ = $\frac{3}{\sqrt{10}}$ C. tan$\frac{α}{2}$ = $\frac{\sqrt{6}}{2}$ D. Cả 3 khẳng định trên đều sai",
        "Question 1: What is the value of sin(30°)?",
        "Câu 12: Tính đạo hàm của hàm số y = x^2 + 3x - 1"
    ]
    
    print("\n🧪 TESTING TEXT CLEANING FUNCTION")
    print("=" * 80)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 Test Case {i}:")
        print(f"📥 Input:  {test_case}")
        
        cleaned = clean_quiz_text(test_case)
        processed = process_math_content(cleaned)
        
        print(f"🧹 Cleaned: {cleaned}")
        print(f"🔬 Final:   {processed}")
        print("-" * 50)

# --- Entry point với test option ---
if __name__ == "__main__":
    try:
        # Option to test text cleaning first
        test_mode = input("Test text cleaning function first? (y/N): ").strip().lower()
        if test_mode == 'y':
            test_text_cleaning()
            
        proceed = input("\nProceed with full quiz scraping? (Y/n): ").strip().lower()
        if proceed != 'n':
            run_quiz_only_scraper()
    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()