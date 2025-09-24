import os
import json
from glob import glob
from urllib.parse import urlparse
import requests
import ijson
from ollama import Ollama  # Ollama Python SDK

ollama_client = Ollama()  # khởi tạo client

def load_json_from_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            parser = ijson.items(f, "item")
            for obj in parser:
                yield obj
    except Exception as e:
        print(f"Lỗi đọc JSON bằng ijson: {e}, thử đọc JSONL")
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
    json_files = glob(os.path.join(folder_path, "*.json"))
    for file in json_files:
        yield from load_json_from_file(file)

def load_json_from_url(url):
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    for obj in data:
        yield obj

def query_ollama_sdk(batch_to_process, model="llama3.2:latest"):
    """Gọi Ollama Python SDK, trả về list dict đã điền answer"""
    prompt = (
        "Bạn là chuyên gia vật lý, hãy điền đáp án đúng cho từng câu hỏi dưới đây. "
        "Trả lời theo JSON, giữ nguyên key 'question' và 'options', chỉ điền 'answer'.\n\n"
    )
    prompt += json.dumps(batch_to_process, ensure_ascii=False)
    try:
        response = ollama_client.create(
            model=model,
            prompt=prompt,
            temperature=0
        )
        # Ollama SDK trả về text, parse JSON
        return json.loads(response.text)
    except Exception as e:
        print(f"Lỗi parsing JSON từ Ollama SDK: {e}")
        return batch_to_process  # fallback trả batch gốc

def fill_answers_stream(generator, batch_size=20, model="llama3.2:latest"):
    batch = []
    for obj in generator:
        batch.append(obj)
        if len(batch) >= batch_size:
            yield from fill_and_return_batch(batch, model)
            batch = []
    if batch:
        yield from fill_and_return_batch(batch, model)

def fill_and_return_batch(batch, model):
    batch_to_process = [q for q in batch if q.get("answer") is None]
    if batch_to_process:
        updated_batch = query_ollama_sdk(batch_to_process, model)
        for ub in updated_batch:
            for original in batch:
                if ub["question"] == original["question"]:
                    original["answer"] = ub.get("answer")
    return batch

def main():
    source = input("Nhập đường dẫn file JSON/JSONL, folder, hoặc URL: ").strip().strip("'\"")
    if not source:
        print("Không có đường dẫn!")
        return

    if os.path.isfile(source):
        generator = load_json_from_file(source)
        base_path = os.path.dirname(source)
        base_name = os.path.splitext(os.path.basename(source))[0]
    elif os.path.isdir(source):
        generator = load_json_from_folder(source)
        base_path = source
        base_name = "merged"
    elif urlparse(source).scheme in ("http", "https"):
        generator = load_json_from_url(source)
        base_path = os.getcwd()
        base_name = "downloaded"
    else:
        print("Lựa chọn không hợp lệ!")
        return

    out_file = os.path.join(base_path, f"{base_name}_fillnull.json")
    print(f"Đang điền các câu answer null và ghi kết quả vào: {out_file}")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("[\n")
        first = True
        for obj in fill_answers_stream(generator, batch_size=20):
            if not first:
                f.write(",\n")
            else:
                first = False
            json.dump(obj, f, ensure_ascii=False)
        f.write("\n]")

    print(f"Đã ghi xong: {out_file}")

if __name__ == "__main__":
    main()