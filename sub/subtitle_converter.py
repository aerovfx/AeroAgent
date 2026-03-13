import os
import re
import io
import argparse
import chardet
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import os
import re
import io
import argparse
import chardet
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Configuration
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SUBTITLE_EXTENSIONS = {'.srt', '.vtt', '.ass', '.ssa', '.sub', '.sbv'}
TOKEN_PATH = 'token.pickle'
CREDENTIALS_PATH = 'credentials.json'  # Download from Google Cloud Console


def authenticate():
    """Authenticate and return a Drive service instance."""
    creds = None
    if os.path.exists(TOKEN_PATH):
        try:
            with open(TOKEN_PATH, 'rb') as f:
                creds = pickle.load(f)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_PATH):
                raise FileNotFoundError(
                    f"Credentials file '{CREDENTIALS_PATH}' not found."
                )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as f:
            pickle.dump(creds, f)

    return build('drive', 'v3', credentials=creds)


def list_drive_items(service, folder_id):
    """List files and folders in a Drive folder."""
    items = []
    page_token = None
    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            spaces='drive',
            fields='nextPageToken, files(id, name, mimeType)',
            pageToken=page_token,
        ).execute()
        items.extend(response.get('files', []))
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    return items


def download_file(service, file_id):
    """Download a file from Drive and return its bytes."""
    request = service.files().get_media(fileId=file_id)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    buffer.seek(0)
    return buffer.read()


def decode_content(raw_bytes):
    """Detect encoding and decode bytes to str."""
    detected = chardet.detect(raw_bytes)
    encoding = detected.get('encoding') or 'utf-8'
    try:
        return raw_bytes.decode(encoding)
    except (UnicodeDecodeError, LookupError):
        return raw_bytes.decode('utf-8', errors='replace')


# Converters
def vtt_to_srt(content: str) -> str:
    lines = content.splitlines()
    result = []
    counter = 1
    i = 0

    # skip header until first timestamp
    while i < len(lines) and not re.search(r"\d{2}:\d{2}", lines[i]):
        i += 1

    while i < len(lines):
        line = lines[i].strip()
        time_match = re.match(
            r"(\d{2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[.,]\d{3})",
            line,
        )
        if time_match:
            start = time_match.group(1).replace('.', ',')
            end = time_match.group(2).replace('.', ',')
            i += 1
            texts = []
            while i < len(lines) and lines[i].strip():
                clean = re.sub(r'<[^>]+>', '', lines[i])
                texts.append(clean)
                i += 1
            if texts:
                result.append(str(counter))
                result.append(f"{start} --> {end}")
                result.extend(texts)
                result.append('')
                counter += 1
        i += 1

    return '\n'.join(result)


def ass_to_srt(content: str) -> str:
    result = []
    counter = 1
    in_events = False

    for line in content.splitlines():
        if line.strip().lower() == '[events]':
            in_events = True
            continue

        if in_events and line.startswith('Dialogue:'):
            parts = line.split(',', 9)
            if len(parts) < 10:
                continue
            start_raw = parts[1].strip()
            end_raw = parts[2].strip()
            text_raw = parts[9].strip()

            def convert_time(t):
                t = t.strip()
                match = re.match(r"(\d+):(\d{2}):(\d{2})\.(\d{2})", t)
                if match:
                    h, m, s, cs = match.groups()
                    ms = int(cs) * 10
                    return f"{int(h):02d}:{m}:{s},{ms:03d}"
                return t

            start = convert_time(start_raw)
            end = convert_time(end_raw)

            text = re.sub(r'\{[^}]+\}', '', text_raw)
            text = text.replace('\\N', '\n').replace('\\n', '\n')

            if text.strip():
                result.append(str(counter))
                result.append(f"{start} --> {end}")
                result.append(text)
                result.append('')
                counter += 1

    return '\n'.join(result)


def sbv_to_srt(content: str) -> str:
    result = []
    counter = 1
    lines = content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        time_match = re.match(r"(\d+:\d{2}:\d{2}\.\d{3}),(\d+:\d{2}:\d{2}\.\d{3})", line)
        if time_match:
            start = time_match.group(1).replace('.', ',')
            end = time_match.group(2).replace('.', ',')
            i += 1
            texts = []
            while i < len(lines) and lines[i].strip():
                texts.append(lines[i])
                i += 1
            if texts:
                result.append(str(counter))
                result.append(f"{start} --> {end}")
                result.extend(texts)
                result.append('')
                counter += 1
        i += 1

    return '\n'.join(result)


def srt_to_vtt(content: str) -> str:
    """Convert SRT text to a simple WebVTT text."""
    lines = content.splitlines()
    out = ['WEBVTT', '']
    for line in lines:
        # convert timestamp commas to dots in timestamp lines
        if '-->' in line:
            out.append(line.replace(',', '.'))
        else:
            out.append(line)
    return '\n'.join(out)


def sub_to_srt(content: str, fps: float = 25.0) -> str:
    result = []
    counter = 1

    for line in content.splitlines():
        match = re.match(r"\{(\d+)\}\{(\d+)\}(.*)", line)
        if match:
            start_frame = int(match.group(1))
            end_frame = int(match.group(2))
            text = match.group(3).replace('|', '\n')

            def frames_to_srt_time(frames, fps):
                total_ms = int(frames / fps * 1000)
                h = total_ms // 3600000
                m = (total_ms % 3600000) // 60000
                s = (total_ms % 60000) // 1000
                ms = total_ms % 1000
                return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

            start = frames_to_srt_time(start_frame, fps)
            end = frames_to_srt_time(end_frame, fps)

            result.append(str(counter))
            result.append(f"{start} --> {end}")
            result.append(text)
            result.append('')
            counter += 1

    return '\n'.join(result)


def convert_subtitle(content: str, source_ext: str, target_format: str = 'srt') -> str:
    src = source_ext.lower()
    if src == '.srt':
        return content

    if target_format == 'srt':
        if src == '.vtt':
            return vtt_to_srt(content)
        elif src in ('.ass', '.ssa'):
            return ass_to_srt(content)
        elif src == '.sbv':
            return sbv_to_srt(content)
        elif src == '.sub':
            return sub_to_srt(content)

    raise ValueError(f"Unsupported convert {src} -> {target_format}")


def process_folder(service, folder_id, folder_name, local_path, target_format, stats):
    print(f"\n📁 Processing: {folder_name}")
    os.makedirs(local_path, exist_ok=True)

    items = list_drive_items(service, folder_id)

    for item in items:
        name = item['name']
        mime = item.get('mimeType')

        if mime == 'application/vnd.google-apps.folder':
            sub_path = os.path.join(local_path, sanitize_name(name))
            process_folder(service, item['id'], name, sub_path, target_format, stats)
        else:
            ext = Path(name).suffix.lower()
            if ext in SUBTITLE_EXTENSIONS:
                try:
                    print(f"  ⬇️  Downloading: {name}")
                    raw = download_file(service, item['id'])
                    print(f"    raw bytes: {len(raw)}")
                    content = decode_content(raw)
                    print(f"    decoded len: {len(content)}")

                    # optionally save original bytes
                    if target_format.get('download_original'):
                        stem = Path(name).stem
                        orig_name = f"{stem}{ext}"
                        orig_path = os.path.join(local_path, orig_name)
                        with open(orig_path, 'wb') as f:
                            f.write(raw)
                        print(f"    ✅ Saved original: {orig_path}")

                    # produce requested formats
                    save_formats = target_format.get('save_formats', ['srt'])
                    # ensure we can get srt content first if needed
                    srt_content = None
                    if 'srt' in save_formats:
                        if ext == '.srt':
                            srt_content = content
                        else:
                            try:
                                srt_content = convert_subtitle(content, ext, 'srt')
                            except Exception as e:
                                print(f"    ⚠️ convert to srt failed for {name}: {e}")

                    for fmt in save_formats:
                        out_text = None
                        if fmt == 'srt':
                            if srt_content is not None:
                                out_text = srt_content
                        elif fmt == 'vtt':
                            if ext == '.vtt':
                                out_text = content
                            else:
                                # convert via srt
                                if srt_content is None:
                                    try:
                                        srt_content = convert_subtitle(content, ext, 'srt')
                                    except Exception as e:
                                        print(f"    ⚠️ convert to srt failed for vtt conversion {name}: {e}")
                                if srt_content is not None:
                                    out_text = srt_to_vtt(srt_content)

                        if out_text is not None:
                            stem = Path(name).stem
                            out_name = f"{stem}.{fmt}"
                            out_path = os.path.join(local_path, out_name)
                            with open(out_path, 'w', encoding='utf-8') as f:
                                f.write(out_text)
                            print(f"    ✅ Saved: {out_path}")
                            stats['success'] += 1
                        else:
                            print(f"    ⚠️ No output for format {fmt} for {name}")
                            stats['error'] += 1
                except Exception as e:
                    print(f"  ❌ Error processing {name}: {e}")
                    stats['error'] += 1


def sanitize_name(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def main():
    parser = argparse.ArgumentParser(description='Download subtitle files from Google Drive and save as .srt/.vtt.')
    parser.add_argument('--folder-id', '-f', required=True, help='Root Drive folder ID')
    parser.add_argument('--output-dir', '-o', default='./subtitles_output', help='Local output directory')
    parser.add_argument('--save-formats', default='srt,vtt', help='Comma-separated output formats to save (e.g. srt,vtt)')
    parser.add_argument('--download-original', action='store_true', help='Also save the original file bytes')
    parser.add_argument('--folder-name', '-n', default='Drive_Subtitles', help='Local root folder name')

    args = parser.parse_args()

    print("🔐 Authenticating Google Drive...")
    service = authenticate()
    print("✅ Authenticated\n")

    stats = {'success': 0, 'error': 0}
    root_local = os.path.join(args.output_dir, sanitize_name(args.folder_name))

    target_format_opts = {
        'save_formats': [x.strip() for x in args.save_formats.split(',') if x.strip()],
        'download_original': args.download_original,
    }

    process_folder(
        service=service,
        folder_id=args.folder_id,
        folder_name=args.folder_name,
        local_path=root_local,
        target_format=target_format_opts,
        stats=stats,
    )

    print('\n' + '=' * 50)
    print('🎉 Done!')
    print(f"   ✅ Success : {stats['success']} files")
    print(f"   ❌ Errors  : {stats['error']} files")
    print(f"   📂 Saved at: {os.path.abspath(root_local)}")


if __name__ == '__main__':
    main()