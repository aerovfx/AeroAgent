from datasets import load_dataset
import os

# Unset token tạm thời nếu invalid (hoặc set đúng token)
os.environ.pop('HF_TOKEN', None)  # Bỏ token env
# Hoặc: os.environ['HF_TOKEN'] = 'your_valid_hf_token_here'  # Nếu cần private

repo_name = "aerovfx/physic"
try:
    ds = load_dataset(repo_name, split="train")
    print(f"Dataset loaded successfully!")
    print(f"Size: {len(ds)} rows")
    print(f"Sample: {ds[0]}")  # In example đầu
except Exception as e:
    print(f"Load failed: {e}")
    # Fallback: Thử public mode
    from huggingface_hub import HfApi
    api = HfApi()
    info = api.dataset_info(repo_name)
    print(f"Dataset info: {info.card_data if info.card_data else 'No card data'}")