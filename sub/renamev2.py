import os
import re

# ====== NHẬP THƯ MỤC ======
root_dir = input("Nhập đường dẫn thư mục cần đổi tên: ").strip()

if not os.path.isdir(root_dir):
    print("❌ Thư mục không tồn tại!")
    exit()

prefix = "aero_LLM_"

# Pattern cho file dạng: 1 -For loops.en_US.vtt
pattern = re.compile(r'^(\d+)\s*-\s*(.*?)\.en_US\.vtt$', re.IGNORECASE)

files_to_rename = []

# ====== QUÉT FILE (bao gồm subfolder) ======
for root, dirs, files in os.walk(root_dir):
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            name_part = match.group(2).strip()

            new_filename = f"{prefix}{number:02d}_{name_part}.md"

            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)

            files_to_rename.append((old_path, new_path))

# ====== PREVIEW ======
if not files_to_rename:
    print("Không tìm thấy file phù hợp.")
    exit()

print("\n📋 Danh sách file sẽ được đổi tên:\n")
for old, new in files_to_rename:
    print(f"{old}")
    print(f"→ {new}\n")

# ====== XÁC NHẬN ======
confirm = input("Bạn có muốn tiếp tục không? (y/n): ").lower()

if confirm == 'y':
    for old, new in files_to_rename:
        os.rename(old, new)
    print("\n✅ Đổi tên hoàn tất.")
else:
    print("\n⛔ Đã huỷ thao tác.")