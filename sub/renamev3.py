import os

# ====== NHẬP THƯ MỤC GỐC ======
root_dir = input("Nhập đường dẫn thư mục docs: ").strip()

if not os.path.isdir(root_dir):
    print("❌ Thư mục không tồn tại!")
    exit()

old_prefix = "aero_LL_"
new_prefix = "aero_LLM_"

files_to_rename = []

# ====== QUÉT TOÀN BỘ THƯ MỤC CON ======
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.startswith(old_prefix):
            new_filename = new_prefix + file[len(old_prefix):]

            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)

            files_to_rename.append((old_path, new_path))

# ====== PREVIEW ======
if not files_to_rename:
    print("⚠️ Không tìm thấy file nào cần đổi tên.")
    exit()

print("\n📋 Danh sách file sẽ được đổi tên:\n")
for old, new in files_to_rename:
    print(old)
    print("→", new, "\n")

# ====== XÁC NHẬN ======
confirm = input("Bạn có muốn tiếp tục không? (y/n): ").lower()

if confirm == "y":
    for old, new in files_to_rename:
        os.rename(old, new)
    print("\n✅ Đổi tên hoàn tất.")
else:
    print("\n⛔ Đã huỷ thao tác.")