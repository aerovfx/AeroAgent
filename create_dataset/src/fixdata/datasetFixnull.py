import os
import json
import subprocess
from glob import glob
from urllib.parse import urlparse
import requests
import ijson

def load_json_from_file(path):
    """Stream đọc file JSON lớn, trả về generator object"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            parser = ijson.items(f, "item")
            for obj in parser:
                yield obj
    except Exception as e:
        print(f"Lỗi đọc JSON bằng ijson: {e}")
        # fallback: thử JSONL (mỗi dòng 1 object)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except Exception as e2:
                    print(f"Lỗi JSON ở dòng: {line[:50]}... -> {e2}")

def load_json_from_folder(folder_path):
    """Load tất cả JSON trong folder"""
    json_files = glob(os.path.join(folder_path, "*.json"))
    for file in json_files:
        yield from load_json_from_file(file)

def load_json_from_url(url):
    """Tải JSON trực tiếp từ link"""
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    for obj in data:
        yield obj

def query_ollama(prompt, model="llama3.2:latest"):
    """Gọi Ollama CLI phiên bản mới"""
    result = subprocess.run(
        ["ollama", "run", model, "--prompt", prompt],
        stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").strip()

def fill_answers_stream(generator, batch_size=20, model="llama2"):
    """Điền answer còn null theo batch, trả về generator"""
    batch = []
    for obj in generator:
        batch.append(obj)
        if len(batch) >= batch_size:
            batch = fill_batch(batch, model)
            for b in batch:
                yield b
            batch = []
    if batch:
        batch = fill_batch(batch, model)
        for b in batch:
            yield b

def fill_batch(batch, model):
    batch_to_process = [q for q in batch if q.get("answer") is None]
    if not batch_to_process:
        return batch
    prompt = (
        "Bạn là chuyên gia vật lý, hãy điền đáp án đúng cho từng câu hỏi dưới đây. "
        "Trả lời theo JSON, giữ nguyên key 'question' và 'options', chỉ điền 'answer'.\n\n"
    )
    prompt += json.dumps(batch_to_process, ensure_ascii=False)
    try:
        answer_json = query_ollama(prompt, model=model)
        updated_batch = json.loads(answer_json)
        for ub in updated_batch:
            for original in batch:
                if ub["question"] == original["question"]:
                    original["answer"] = ub.get("answer")
    except Exception as e:
        print(f"Lỗi parsing JSON từ Ollama: {e}")
    return batch

def main():
    source = input("Nhập đường dẫn file JSON/JSONL, folder, hoặc URL: ").strip().strip("'\"")
    if not source:
        print("Không có đường dẫn!")
        return

    # Xác định nguồn dữ liệu
    if os.path.isfile(source):
        print("Đang đọc dữ liệu...")
        generator = load_json_from_file(source)
        base_path = os.path.dirname(source)
        base_name = os.path.splitext(os.path.basename(source))[0]
    elif os.path.isdir(source):
        print("Đang đọc dữ liệu từ thư mục...")
        generator = load_json_from_folder(source)
        base_path = source
        base_name = "merged"
    elif urlparse(source).scheme in ("http", "https"):
        print("Đang tải dữ liệu từ URL...")
        generator = load_json_from_url(source)
        base_path = os.getcwd()
        base_name = "downloaded"
    else:
        print("Lựa chọn không hợp lệ!")
        return

    out_file = os.path.join(base_path, f"{base_name}_fillnull.json")
    print(f"Đang điền các câu answer null và ghi kết quả vào: {out_file}")

    # Ghi JSON streaming
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("[\n")
        first = True
        for obj in fill_answers_stream(generator):
            if not first:
                f.write(",\n")
            else:
                first = False
            json.dump(obj, f, ensure_ascii=False)
        f.write("\n]")

    print(f"Đã ghi xong: {out_file}")

if __name__ == "__main__":
    main()