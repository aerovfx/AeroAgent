import pandas as pd
import os

def parquet_to_json(parquet_path, json_path):
    try:
        df = pd.read_parquet(parquet_path)
        print(f"✅ Đã đọc file Parquet: {parquet_path} ({len(df)} dòng, {len(df.columns)} cột)")
        df.to_json(json_path, orient="records", lines=True, force_ascii=False)
        print(f"✅ Đã xuất ra JSON: {json_path}")
    except Exception as e:
        print(f"❌ Lỗi với file {parquet_path}: {e}")

def main():
    print("📂 Chuyển đổi file Parquet sang JSON")
    input_path = input("Nhập đường dẫn file Parquet hoặc thư mục chứa các file Parquet: ").strip().strip("'\"")
    
    if not os.path.exists(input_path):
        print(f"❌ Đường dẫn không tồn tại: {input_path}")
        return
    
    # Nếu là file
    if os.path.isfile(input_path):
        if input_path.endswith(".parquet"):
            json_path = input_path.rsplit(".", 1)[0] + ".json"
            parquet_to_json(input_path, json_path)
        else:
            print("❌ Đây không phải file Parquet")
    
    # Nếu là folder
    elif os.path.isdir(input_path):
        parquet_files = [f for f in os.listdir(input_path) if f.endswith(".parquet")]
        if not parquet_files:
            print("❌ Không tìm thấy file Parquet trong thư mục")
            return
        for f in parquet_files:
            parquet_path = os.path.join(input_path, f)
            json_path = os.path.join(input_path, f.rsplit(".", 1)[0] + ".json")
            parquet_to_json(parquet_path, json_path)
    else:
        print("❌ Đường dẫn không hợp lệ")

if __name__ == "__main__":
    main()