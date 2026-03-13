"""
drive_subtitle_whisper.py
=========================
1. Kết nối Google Drive, duyệt qua folder (kể cả sub-folder).
2. Với mỗi video trên Drive:
   - Nếu đã có file phụ đề (.srt/.vtt/.ass/.ssa/.sub/.sbv) cùng tên → tải về, convert sang .srt + .txt.
   - Nếu chưa có phụ đề → tải video về tạm, dùng Whisper tạo .srt + .vtt + .txt.
3. Lưu file theo đúng cấu trúc thư mục như trên Drive.

Yêu cầu:
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2
    pip install openai-whisper torch tqdm chardet

Chạy:
    python drive_subtitle_whisper.py --folder-id <DRIVE_FOLDER_ID> --output-dir ./output
"""

import os
import re
import io
import gc
import time
import pickle
import argparse
import tempfile
import warnings
import multiprocessing
from pathlib import Path

import chardet
import torch
import whisper
from tqdm import tqdm
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")
warnings.filterwarnings("ignore", category=UserWarning)

# ─────────────────────────────────────────────
# CẤU HÌNH
# ─────────────────────────────────────────────
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
TOKEN_PATH = "token.pickle"
CREDENTIALS_PATH = "credentials.json"

SUBTITLE_EXTENSIONS = {".srt", ".vtt", ".ass", ".ssa", ".sub", ".sbv"}
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".m4v", ".webm"}
GOOGLE_FOLDER_MIME = "application/vnd.google-apps.folder"

WHISPER_MODEL_SIZE = "medium"  # tiny / base / small / medium / large


# ─────────────────────────────────────────────
# XÁC THỰC GOOGLE DRIVE
# ─────────────────────────────────────────────
def authenticate():
    creds = None
    if os.path.exists(TOKEN_PATH):
        try:
            with open(TOKEN_PATH, "rb") as f:
                creds = pickle.load(f)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_PATH):
                raise FileNotFoundError(
                    f"Không tìm thấy '{CREDENTIALS_PATH}'. "
                    "Hãy tải về từ Google Cloud Console."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "wb") as f:
            pickle.dump(creds, f)

    return build("drive", "v3", credentials=creds)


# ─────────────────────────────────────────────
# TIỆN ÍCH DRIVE
# ─────────────────────────────────────────────
def list_drive_items(service, folder_id):
    """Liệt kê tất cả file/folder trong một thư mục Drive."""
    items = []
    page_token = None
    while True:
        resp = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            spaces="drive",
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=page_token,
        ).execute()
        items.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return items


def download_file_bytes(service, file_id) -> bytes:
    """Tải file từ Drive, trả về bytes."""
    request = service.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    buf.seek(0)
    return buf.read()


def download_file_to_path(service, file_id, dest_path: str):
    """Tải file từ Drive, ghi ra đĩa."""
    raw = download_file_bytes(service, file_id)
    with open(dest_path, "wb") as f:
        f.write(raw)


# ─────────────────────────────────────────────
# DECODE VÀ CONVERT SUBTITLE
# ─────────────────────────────────────────────
def decode_content(raw_bytes: bytes) -> str:
    detected = chardet.detect(raw_bytes)
    encoding = detected.get("encoding") or "utf-8"
    try:
        return raw_bytes.decode(encoding)
    except (UnicodeDecodeError, LookupError):
        return raw_bytes.decode("utf-8", errors="replace")


def vtt_to_srt(content: str) -> str:
    lines = content.splitlines()
    result, counter, i = [], 1, 0
    while i < len(lines) and not re.search(r"\d{2}:\d{2}", lines[i]):
        i += 1
    while i < len(lines):
        line = lines[i].strip()
        tm = re.match(
            r"(\d{2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[.,]\d{3})", line
        )
        if tm:
            start = tm.group(1).replace(".", ",")
            end = tm.group(2).replace(".", ",")
            i += 1
            texts = []
            while i < len(lines) and lines[i].strip():
                texts.append(re.sub(r"<[^>]+>", "", lines[i]))
                i += 1
            if texts:
                result += [str(counter), f"{start} --> {end}"] + texts + [""]
                counter += 1
        i += 1
    return "\n".join(result)


def ass_to_srt(content: str) -> str:
    result, counter, in_events = [], 1, False
    for line in content.splitlines():
        if line.strip().lower() == "[events]":
            in_events = True
            continue
        if in_events and line.startswith("Dialogue:"):
            parts = line.split(",", 9)
            if len(parts) < 10:
                continue

            def ct(t):
                m = re.match(r"(\d+):(\d{2}):(\d{2})\.(\d{2})", t.strip())
                if m:
                    h, mi, s, cs = m.groups()
                    return f"{int(h):02d}:{mi}:{s},{int(cs)*10:03d}"
                return t

            start, end = ct(parts[1]), ct(parts[2])
            text = re.sub(r"\{[^}]+\}", "", parts[9].strip())
            text = text.replace("\\N", "\n").replace("\\n", "\n")
            if text.strip():
                result += [str(counter), f"{start} --> {end}", text, ""]
                counter += 1
    return "\n".join(result)


def sbv_to_srt(content: str) -> str:
    result, counter, lines, i = [], 1, content.splitlines(), 0
    while i < len(lines):
        tm = re.match(r"(\d+:\d{2}:\d{2}\.\d{3}),(\d+:\d{2}:\d{2}\.\d{3})", lines[i].strip())
        if tm:
            start, end = tm.group(1).replace(".", ","), tm.group(2).replace(".", ",")
            i += 1
            texts = []
            while i < len(lines) and lines[i].strip():
                texts.append(lines[i])
                i += 1
            if texts:
                result += [str(counter), f"{start} --> {end}"] + texts + [""]
                counter += 1
        i += 1
    return "\n".join(result)


def sub_to_srt(content: str, fps: float = 25.0) -> str:
    result, counter = [], 1
    for line in content.splitlines():
        m = re.match(r"\{(\d+)\}\{(\d+)\}(.*)", line)
        if m:
            def f2t(fr):
                ms = int(int(fr) / fps * 1000)
                return f"{ms//3600000:02d}:{(ms%3600000)//60000:02d}:{(ms%60000)//1000:02d},{ms%1000:03d}"
            text = m.group(3).replace("|", "\n")
            result += [str(counter), f"{f2t(m.group(1))} --> {f2t(m.group(2))}", text, ""]
            counter += 1
    return "\n".join(result)


def convert_to_srt(content: str, ext: str) -> str:
    ext = ext.lower()
    if ext == ".srt":
        return content
    if ext == ".vtt":
        return vtt_to_srt(content)
    if ext in (".ass", ".ssa"):
        return ass_to_srt(content)
    if ext == ".sbv":
        return sbv_to_srt(content)
    if ext == ".sub":
        return sub_to_srt(content)
    raise ValueError(f"Không hỗ trợ định dạng: {ext}")


def srt_to_txt(srt_content: str) -> str:
    """Trích xuất văn bản thuần từ nội dung SRT."""
    lines = srt_content.splitlines()
    texts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}", line):
            continue
        texts.append(line)
    return "\n".join(texts)


def srt_to_vtt(srt_content: str) -> str:
    """Convert SRT sang WebVTT."""
    vtt = "WEBVTT\n\n"
    vtt += srt_content.replace(",", ".", 1)
    # Thay dấu phẩy trong timestamp
    def fix_ts(m):
        return m.group(0).replace(",", ".")
    vtt = re.sub(r"\d{2}:\d{2}:\d{2},\d{3}", fix_ts, srt_content)
    return "WEBVTT\n\n" + vtt


# ─────────────────────────────────────────────
# WHISPER HELPERS
# ─────────────────────────────────────────────
def format_time_srt(t: float) -> str:
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    ms = (s - int(s)) * 1000
    return f"{int(h):02}:{int(m):02}:{int(s):02},{int(ms):03}"


def format_time_vtt(t: float) -> str:
    return format_time_srt(t).replace(",", ".")


def segments_to_srt(segments) -> str:
    lines = []
    for i, seg in enumerate(segments, 1):
        lines.append(str(i))
        lines.append(f"{format_time_srt(seg['start'])} --> {format_time_srt(seg['end'])}")
        lines.append(seg["text"].strip())
        lines.append("")
    return "\n".join(lines)


def segments_to_vtt(segments) -> str:
    lines = ["WEBVTT", ""]
    for i, seg in enumerate(segments, 1):
        lines.append(str(i))
        lines.append(f"{format_time_vtt(seg['start'])} --> {format_time_vtt(seg['end'])}")
        lines.append(seg["text"].strip())
        lines.append("")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# XỬ LÝ CHÍNH
# ─────────────────────────────────────────────
def sanitize_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def save_subtitle_files(stem_path: str, srt_content: str, save_vtt: bool = True):
    """Ghi .srt, tùy chọn .vtt, và .txt từ nội dung SRT."""
    srt_path = stem_path + ".srt"
    txt_path = stem_path + ".txt"

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    print(f"      💾 SRT: {srt_path}")

    if save_vtt:
        vtt_path = stem_path + ".vtt"
        with open(vtt_path, "w", encoding="utf-8") as f:
            f.write(srt_to_vtt(srt_content))
        print(f"      💾 VTT: {vtt_path}")

    txt_content = srt_to_txt(srt_content)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(txt_content)
    print(f"      💾 TXT: {txt_path}")


def process_folder(
    service,
    folder_id: str,
    folder_name: str,
    local_path: str,
    whisper_model,
    device: str,
    fp16: bool,
    stats: dict,
):
    print(f"\n📁 Thư mục: {folder_name}")
    os.makedirs(local_path, exist_ok=True)

    items = list_drive_items(service, folder_id)

    # Lập index tên file (không có đuôi) để tra nhanh
    # name_stem → list of items
    name_index: dict[str, list] = {}
    for item in items:
        stem = Path(item["name"]).stem.lower()
        name_index.setdefault(stem, []).append(item)

    processed_stems = set()

    for item in items:
        name = item["name"]
        mime = item.get("mimeType", "")
        ext = Path(name).suffix.lower()

        # Đệ quy vào sub-folder
        if mime == GOOGLE_FOLDER_MIME:
            sub_local = os.path.join(local_path, sanitize_name(name))
            process_folder(
                service, item["id"], name, sub_local,
                whisper_model, device, fp16, stats
            )
            continue

        stem = Path(name).stem
        stem_lower = stem.lower()

        # ── Trường hợp 1: File là phụ đề ──────────────────────────────
        if ext in SUBTITLE_EXTENSIONS:
            out_stem = os.path.join(local_path, sanitize_name(stem))
            if stem_lower in processed_stems:
                continue  # Đã xử lý qua video cùng tên
            print(f"\n  📝 Phụ đề: {name}")
            try:
                raw = download_file_bytes(service, item["id"])
                content = decode_content(raw)
                srt = convert_to_srt(content, ext)
                save_subtitle_files(out_stem, srt, save_vtt=True)
                processed_stems.add(stem_lower)
                stats["subtitle_downloaded"] += 1
            except Exception as e:
                print(f"  ❌ Lỗi tải phụ đề {name}: {e}")
                stats["error"] += 1
            continue

        # ── Trường hợp 2: File là video ───────────────────────────────
        if ext not in VIDEO_EXTENSIONS:
            continue

        if stem_lower in processed_stems:
            continue  # Đã xử lý (có phụ đề trùng tên trước đó)

        out_stem = os.path.join(local_path, sanitize_name(stem))

        # Kiểm tra xem Drive có file phụ đề cùng tên không
        existing_sub = None
        for sibling in name_index.get(stem_lower, []):
            sib_ext = Path(sibling["name"]).suffix.lower()
            if sib_ext in SUBTITLE_EXTENSIONS:
                existing_sub = sibling
                break

        if existing_sub:
            # Tải phụ đề có sẵn
            print(f"\n  🎬 Video: {name}")
            print(f"  ✅ Đã có phụ đề: {existing_sub['name']} → tải về và convert")
            try:
                raw = download_file_bytes(service, existing_sub["id"])
                content = decode_content(raw)
                srt = convert_to_srt(content, Path(existing_sub["name"]).suffix)
                save_subtitle_files(out_stem, srt, save_vtt=True)
                processed_stems.add(stem_lower)
                stats["subtitle_downloaded"] += 1
            except Exception as e:
                print(f"  ❌ Lỗi: {e}")
                stats["error"] += 1
        else:
            # Dùng Whisper tạo phụ đề mới
            print(f"\n  🎬 Video: {name} — Không có phụ đề → Dùng Whisper")
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
                tmp_path = tmp.name
            try:
                print(f"  ⬇️  Đang tải video tạm...")
                download_file_to_path(service, item["id"], tmp_path)

                print(f"  🎙️  Đang nhận dạng giọng nói...")
                result = whisper_model.transcribe(
                    tmp_path,
                    fp16=fp16,
                    verbose=False,
                    task="transcribe",
                    condition_on_previous_text=False,
                    temperature=0.0,
                    compression_ratio_threshold=2.4,
                    no_speech_threshold=0.6,
                )

                if not result["segments"]:
                    print(f"  ⚠️  Không phát hiện giọng nói trong {name}")
                    stats["no_speech"] += 1
                else:
                    srt = segments_to_srt(result["segments"])
                    save_subtitle_files(out_stem, srt, save_vtt=True)
                    processed_stems.add(stem_lower)
                    stats["whisper_generated"] += 1

                del result
                gc.collect()

            except Exception as e:
                print(f"  ❌ Lỗi Whisper với {name}: {e}")
                stats["error"] += 1
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def optimize_for_cpu():
    torch.set_num_threads(multiprocessing.cpu_count())
    print(f"🔧 CPU mode: {multiprocessing.cpu_count()} threads")


def main():
    parser = argparse.ArgumentParser(
        description="Tải phụ đề từ Google Drive hoặc tạo bằng Whisper."
    )
    parser.add_argument("--folder-id", "-f", required=True, help="ID thư mục Drive gốc")
    parser.add_argument("--output-dir", "-o", default="./subtitle_output", help="Thư mục lưu cục bộ")
    parser.add_argument("--folder-name", "-n", default="Drive_Output", help="Tên thư mục gốc cục bộ")
    parser.add_argument("--model", "-m", default=WHISPER_MODEL_SIZE,
                        choices=["tiny", "base", "small", "medium", "large"],
                        help="Kích thước model Whisper")
    args = parser.parse_args()

    # ── Thiết bị ──
    if torch.cuda.is_available():
        device, fp16 = "cuda", True
        print("⚡ Sử dụng GPU CUDA (FP16)")
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device, fp16 = "mps", False
        print("🍎 Sử dụng Apple Silicon MPS (FP32)")
    else:
        device, fp16 = "cpu", False
        optimize_for_cpu()
        print("🐢 Sử dụng CPU (FP32)")

    # ── Load Whisper ──
    print(f"\n📥 Đang tải Whisper model '{args.model}'...")
    whisper_model = whisper.load_model(args.model, device=device)
    print("✅ Whisper sẵn sàng\n")

    # ── Xác thực Drive ──
    print("🔐 Xác thực Google Drive...")
    service = authenticate()
    print("✅ Đã xác thực\n")

    stats = {
        "subtitle_downloaded": 0,
        "whisper_generated": 0,
        "no_speech": 0,
        "error": 0,
    }

    root_local = os.path.join(args.output_dir, sanitize_name(args.folder_name))

    process_folder(
        service=service,
        folder_id=args.folder_id,
        folder_name=args.folder_name,
        local_path=root_local,
        whisper_model=whisper_model,
        device=device,
        fp16=fp16,
        stats=stats,
    )

    print("\n" + "=" * 55)
    print("🎉 Hoàn tất!")
    print(f"   📥 Phụ đề tải về   : {stats['subtitle_downloaded']} file")
    print(f"   🎙️  Whisper tạo mới  : {stats['whisper_generated']} file")
    print(f"   🔇 Không có giọng   : {stats['no_speech']} file")
    print(f"   ❌ Lỗi              : {stats['error']} file")
    print(f"   📂 Lưu tại          : {os.path.abspath(root_local)}")


if __name__ == "__main__":
    main()