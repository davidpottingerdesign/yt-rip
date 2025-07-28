# yt-rip
python script to download youtube audio to make like an audiobook

#Python 3.13.5
#yt-dlp 2025.7.21 from pip
#ffmpeg version 7.1.1-essentials_build-www.gyan.dev

playlist_url = "https://www.youtube.com/playlist?list=PLGQiSf7MYlFknswV4auLQOJ94vYSYKBOx"
        "-filter:a", "atempo=2.0,volume=1.5", #2x speed, 1.5x volume

# Chapter range
start_chapter = 801
end_chapter = 820

ChatGPT generated a lot of this code and I merely resolved some issues to make it work.
The output mp3 files are suitable for my phone, and I can take them hiking or anywhere.
