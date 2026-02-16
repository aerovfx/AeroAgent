import os
import re

# SRT: thời gian dạng 00:00:00,000
SRT_TIME = re.compile(r"^\d{2}:\d{2}:\d{2},\d{3}\s+-->\s+\d{2}:\d{2}:\d{2},\d{3}$")
# VTT: thời gian dạng 00:00:00.000 hoặc 00:00.000
VTT_TIME = re.compile(r"^[\d:.]+\s+-->\s+[\d:.]+$")

def srt_to_txt_file(srt_path, txt_path):
    output_lines = []
    with open(srt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if re.match(r"^\d+$", line):
                continue
            if SRT_TIME.match(line):
                continue
            output_lines.append(line)

    _write_txt(txt_path, output_lines)

def vtt_to_txt_file(vtt_path, txt_path):
    output_lines = []
    with open(vtt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # bỏ header WEBVTT
            if line.startswith("WEBVTT"):
                continue
            # bỏ số thứ tự / cue id
            if re.match(r"^\d+$", line):
                continue
            # bỏ dòng thời gian (00:00:00.000 --> 00:00:00.000)
            if VTT_TIME.match(line):
                continue
            output_lines.append(line)

    _write_txt(txt_path, output_lines)

def _write_txt(txt_path, output_lines):
    if os.path.dirname(txt_path):
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    print(f"✅ Đã lưu: {txt_path}")

def convert_subtitles_folder(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            lower = file.lower()
            if lower.endswith(".srt"):
                srt_path = os.path.join(root, file)
                txt_path = os.path.join(root, file[:-4] + ".txt")
                srt_to_txt_file(srt_path, txt_path)
            elif lower.endswith(".vtt"):
                vtt_path = os.path.join(root, file)
                txt_path = os.path.join(root, file[:-4] + ".txt")
                vtt_to_txt_file(vtt_path, txt_path)

if __name__ == "__main__":
    folder = input("Nhập đường dẫn thư mục chứa file .srt / .vtt: ").strip()
    folder = folder.strip("'\"")
    if os.path.exists(folder):
        convert_subtitles_folder(folder)
        print("✅ Hoàn tất convert tất cả file .srt và .vtt trong thư mục và subfolder.")
    else:
        print("❌ Thư mục không tồn tại!")