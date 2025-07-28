import os
import subprocess
from yt_dlp import YoutubeDL

#Python 3.13.5
#yt-dlp 2025.7.21 from pip
#ffmpeg version 7.1.1-essentials_build-www.gyan.dev

# 🎯 Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLGQiSf7MYlFknswV4auLQOJ94vYSYKBOx"

# 📁 Output folder
output_folder = "Reverend_insanity"
os.makedirs(output_folder, exist_ok=True)

# 🔢 Chapter range
start_chapter = 801
end_chapter = 820

# ⚙ yt-dlp options (no postprocessing here)
ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "force_generic_extractor": False,
    "dump_single_json": True,
}

# 📥 Step 1: Extract all video links from playlist
print("🔎 Gathering playlist info...")
with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(playlist_url, download=False)

entries = info_dict.get("entries", [])
total_chapters = len(entries)

# 🧩 Step 2: Download, process & save
for idx in range(start_chapter - 1, min(end_chapter, total_chapters)):
    entry = entries[idx]
    video_url = f"https://www.youtube.com/watch?v={entry['id']}"
    chapter_number = idx + 1

    temp_filename = f"temp_chapter_{chapter_number}.m4a"
    final_filename = f"RevIns{chapter_number}.mp3"
    final_path = os.path.join(output_folder, final_filename)

    print(f"\n🎬 Chapter {chapter_number}: {entry['title']}")

    # 1️⃣ Download audio only
    print("  ⏬ Downloading audio...")
    download_cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "m4a",
        "-o", temp_filename,
        video_url
    ]
    subprocess.run(download_cmd, check=True)

    # 2️⃣ ffmpeg transform: 2x speed, 1.5x volume
    print("  🎛️ Processing audio (2x speed, +50% volume)...")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", temp_filename,
        "-filter:a", "atempo=2.0,volume=1.5",
        "-vn", final_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3️⃣ Clean up temp file
    os.remove(temp_filename)
    print(f"  ✅ Saved: {final_filename}")

print("\n🎉 All requested chapters processed.")
