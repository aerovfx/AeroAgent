import os
import io
import re
import json
import time
import pickle
import logging
import argparse
from pathlib import Path
from collections import deque

import chardet
from tqdm import tqdm
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError


# =========================
# CONFIG
# =========================
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
TOKEN_PATH = "token.pickle"
CREDENTIALS_PATH = "credentials.json"
STATE_FILE = "download_state.json"

SUBTITLE_EXTENSIONS = {'.srt', '.vtt', '.ass', '.ssa', '.sub', '.sbv'}
BATCH_SIZE = 100
MAX_RETRIES = 5


# =========================
# LOGGING
# =========================
logging.basicConfig(
    filename="drive_sub_stable.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# AUTH
# =========================
def authenticate():
    creds = None

    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, 'wb') as f:
            pickle.dump(creds, f)

    return build('drive', 'v3', credentials=creds)


# =========================
# EXPONENTIAL BACKOFF
# =========================
def execute_with_backoff(request):
    for attempt in range(MAX_RETRIES):
        try:
            return request.execute()
        except HttpError as e:
            if e.resp.status in [429, 500, 502, 503, 504]:
                sleep_time = (2 ** attempt) + (attempt * 0.1)
                logging.warning(f"Retry {attempt+1} after {sleep_time}s")
                time.sleep(sleep_time)
            else:
                raise
    raise Exception("Max retries exceeded")


# =========================
# BFS LIST (NO RECURSION)
# =========================
def list_all_files(service, root_folder_id):
    all_files = []
    queue = deque([(root_folder_id, "")])

    while queue:
        folder_id, current_path = queue.popleft()
        page_token = None

        while True:
            request = service.files().list(
                q=f"'{folder_id}' in parents and trashed=false",
                fields="nextPageToken, files(id, name, mimeType)",
                pageSize=1000,
                pageToken=page_token
            )

            response = execute_with_backoff(request)

            for item in response.get("files", []):
                name = item["name"]
                mime = item["mimeType"]

                if mime == "application/vnd.google-apps.folder":
                    queue.append(
                        (item["id"], os.path.join(current_path, sanitize(name)))
                    )
                else:
                    if Path(name).suffix.lower() in SUBTITLE_EXTENSIONS:
                        item["relative_path"] = current_path
                        all_files.append(item)

            page_token = response.get("nextPageToken")
            if not page_token:
                break

            time.sleep(0.1)

    return all_files


# =========================
# DOWNLOAD FILE
# =========================
def download_file(service, file_id):
    request = service.files().get_media(fileId=file_id)

    for attempt in range(MAX_RETRIES):
        try:
            buffer = io.BytesIO()
            downloader = MediaIoBaseDownload(buffer, request)
            done = False

            while not done:
                _, done = downloader.next_chunk()

            buffer.seek(0)
            return buffer.read()

        except HttpError as e:
            if e.resp.status in [429, 500, 502, 503, 504]:
                sleep_time = (2 ** attempt)
                time.sleep(sleep_time)
            else:
                raise

    raise Exception("Download failed")


# =========================
# UTIL
# =========================
def sanitize(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def decode_bytes(raw):
    detected = chardet.detect(raw)
    encoding = detected.get("encoding") or "utf-8"
    return raw.decode(encoding, errors="replace")


def srt_to_vtt(text):
    lines = text.splitlines()
    out = ["WEBVTT", ""]
    for line in lines:
        if "-->" in line:
            out.append(line.replace(",", "."))
        else:
            out.append(line)
    return "\n".join(out)


# =========================
# STATE MANAGEMENT
# =========================
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    return set()


def save_state(processed_ids):
    with open(STATE_FILE, "w") as f:
        json.dump(list(processed_ids), f)


# =========================
# MAIN
# =========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder-id", required=True)
    parser.add_argument("--output-dir", default="./output")
    parser.add_argument("--save-formats", default="srt,vtt")
    parser.add_argument("--download-original", action="store_true")
    args = parser.parse_args()

    save_formats = [x.strip() for x in args.save_formats.split(",")]

    print("🔐 Authenticating...")
    service = authenticate()

    print("📂 Scanning drive (BFS mode)...")
    files = list_all_files(service, args.folder_id)

    print(f"🚀 Found {len(files)} subtitle files.")

    os.makedirs(args.output_dir, exist_ok=True)

    processed_ids = load_state()
    success = 0
    error = 0

    for i in tqdm(range(0, len(files), BATCH_SIZE)):
        batch = files[i:i + BATCH_SIZE]

        for item in batch:
            if item["id"] in processed_ids:
                continue

            try:
                raw = download_file(service, item["id"])
                content = decode_bytes(raw)

                relative_dir = item.get("relative_path", "")
                output_dir = os.path.join(args.output_dir, relative_dir)
                os.makedirs(output_dir, exist_ok=True)

                stem = Path(item["name"]).stem

                if args.download_original:
                    with open(os.path.join(output_dir, item["name"]), "wb") as f:
                        f.write(raw)

                if "srt" in save_formats:
                    with open(os.path.join(output_dir, stem + ".srt"), "w", encoding="utf-8") as f:
                        f.write(content)

                if "vtt" in save_formats:
                    with open(os.path.join(output_dir, stem + ".vtt"), "w", encoding="utf-8") as f:
                        f.write(srt_to_vtt(content))

                processed_ids.add(item["id"])
                success += 1

            except Exception as e:
                logging.error(f"Error {item['name']}: {e}")
                error += 1

        save_state(processed_ids)

    print("\n" + "=" * 50)
    print("🎉 Done!")
    print(f"✅ Success: {success}")
    print(f"❌ Errors : {error}")
    print("📄 State saved for resume.")


if __name__ == "__main__":
    main()