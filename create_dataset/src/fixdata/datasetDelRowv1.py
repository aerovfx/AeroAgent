# Code này dùng để xoá các rows từ trang 7 đến trang 9 trong dataset "aerovfx/physic"
# và push lại dataset đã fix lên Hugging Face Hub
# để sử dụng cần nhập access token vào dòng dưới nhé, tính toán cẩn thận số dòng cuối để xoá.
import os
from datasets import load_dataset, Dataset

# ⚡ Thay bằng access token Hugging Face của bạn
HF_TOKEN = "hf_xxxxxxx"

# ⚡ Tải dataset từ Hugging Face Hub
dataset = load_dataset("aerovfx/physic", split="train")

print("👉 Trước khi xoá:", len(dataset))

# Giả sử dataset có 829 rows và chia 9 trang
# => Mỗi trang có khoảng 92 rows (829/9 ≈ 92)
rows_per_page = len(dataset) // 9

# Tính index start & end cho trang 7 đến 9
start_idx = rows_per_page * 6   # trang 7 (bắt đầu từ 0-based)
end_idx = len(dataset)          # tới cuối dataset (trang 9)

# Giữ lại các rows từ trang 1 đến 6
dataset_fixed = dataset.select(range(0, start_idx))

print("👉 Sau khi xoá:", len(dataset_fixed))

# ⚡ Push lại dataset đã fix lên Hub
dataset_fixed.push_to_hub(
    "aerovfx/physic",
    token=HF_TOKEN
)