import yt_dlp
import os
import subprocess
import sys

# Get YouTube URL from the user
url = input("Enter the YouTube video link: ").strip()


# Check if VLC Media Player is installed on the system
def find_vlc():
    # VLC default installation paths for Windows
    if sys.platform.startswith("win"):
        paths = [
            r"C:\Program Files\VideoLAN\VLC\vlc.exe",
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
        ]
        for path in paths:
            if os.path.exists(path):
                return path
    return None


# yt-dlp options
opts = {
    # Download only progressive MP4 (video + audio together)
    "format": "best[ext=mp4][acodec!=none][vcodec!=none]",
    # Save file with video title as filename
    "outtmpl": "%(title)s.%(ext)s",
    # Do not download playlists
    "noplaylist": True,
    # Suppress yt-dlp console output
    "quiet": True,
}

try:
    # Download the video
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info)

    print("✅ Video downloaded successfully.")

    # Try to open the video with VLC if available
    vlc_path = find_vlc()
    if vlc_path:
        subprocess.Popen([vlc_path, video_file])

except Exception:
    # Handle cases where the video cannot be downloaded as a progressive MP4
    print("!!This video could not be downloaded as a compatible MP4 file.")
