import sys
import os
from urllib.parse import urlparse, parse_qs

import whisper
import yt_dlp

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def extract_video_id(url):
    """
    Extracts the YouTube video ID from a URL.
    Supports both youtu.be and youtube.com formats.
    """
    parsed = urlparse(url)
    # Short URL format
    if parsed.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed.path.lstrip('/')
    # Standard URL format
    qs = parse_qs(parsed.query)
    return qs.get('v', [None])[0]


def download_audio(youtube_url, video_id):
    """
    Downloads the best audio stream from YouTube and converts it to MP3.
    The output filename will be <video_id>.mp3
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{video_id}.%(ext)s',  # e.g. 7Sa2k4nthgU.mp3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"🔽 Letöltés: {youtube_url}")
        ydl.download([youtube_url])
        print(f"✅ Letöltve: {video_id}.mp3")


def transcribe_audio(audio_path, video_id, language="Hungarian"):  # change language if needed
    """
    Uses OpenAI Whisper to transcribe an MP3 file.
    Saves the result to <video_id>.txt
    """
    print(f"🧠 Átirat készítése: {audio_path}")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language=language)
    #txt_path = f"{video_id}.txt"
    txt_path = "video_Keyword.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"📄 Átirat elmentve: {txt_path}\n")

        # 🔥 MP3 törlése
    try:
        os.remove(audio_path)
        print(f"🗑️ MP3 törölve: {audio_path}\n")
    except OSError as e:
        print(f"⚠️ Nem sikerült törölni az MP3 fájlt: {e}")


if __name__ == "__main__":
    # Check video_textToSpeech.txt exists
    if not os.path.exists('video_textToSpeech.txt'):
        print("❗ Nem találom a video_textToSpeech.txt fájlt. Győződj meg róla, hogy ugyanabban a mappában van, ahol a script fut.")
        sys.exit(1)

    # Read URLs from video_textToSpeech.txt
    with open('video_textToSpeech.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    urls = [line for line in lines if line.startswith('http')]

    if not urls:
        print("❗ Nem találtam YouTube URL-eket a video_textToSpeech.txt fájlban.")
        sys.exit(1)

    # Process each URL
    for url in urls:
        vid_id = extract_video_id(url)
        if not vid_id:
            print(f"⚠️ Nem sikerült kinyerni a videó ID-t: {url}")
            continue

        mp3_file = f"{vid_id}.mp3"
        # Download and transcribe
        download_audio(url, vid_id)
        transcribe_audio(mp3_file, vid_id)
