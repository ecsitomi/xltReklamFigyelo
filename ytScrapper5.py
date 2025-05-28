from googleapiclient.discovery import build
from datetime import datetime, timezone
from langdetect import detect, LangDetectException
from dotenv import load_dotenv
import os

# API kulcsod ide
load_dotenv()
api_key = os.getenv("API_KEY")

# Mai nap kezdete és vége UTC-ben
now = datetime.now(timezone.utc)
start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999)

# YouTube API kliens létrehozása
youtube = build('youtube', 'v3', developerKey=api_key)

# Nyelvdetektáló függvény
def nyelv_magyar_szoveg(szoveg: str) -> bool:
    try:
        return detect(szoveg) == 'hu'
    except LangDetectException:
        return False

# Kimeneti fájl
output_file = "video_Scrapper.txt"

saved_count = 0
checked_count = 0
next_page_token = None

with open(output_file, "w", encoding="utf-8") as f:
    while saved_count < 5:
        request = youtube.search().list(
            part='snippet',
            maxResults=25,
            publishedAfter=start_of_day.isoformat(),
            publishedBefore=end_of_day.isoformat(),
            type='video',
            regionCode='HU',
            relevanceLanguage='hu',
            order='date',
            pageToken=next_page_token
        )
        response = request.execute()

        if 'items' not in response or not response['items']:
            print("Nincs több találat.")
            break

        for item in response['items']:
            checked_count += 1  # minden egyes videót számolunk

            title = item['snippet']['title']
            description = item['snippet'].get('description', '')

            if not (nyelv_magyar_szoveg(title) or nyelv_magyar_szoveg(description)):
                continue

            video_id = item['id']['videoId']
            url = f'https://www.youtube.com/watch?v={video_id}'
            f.write(f"{title}\n{url}\n\n")

            saved_count += 1
            if saved_count >= 10:
                break

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

print(f"Mentés kész: {saved_count} videó elmentve a(z) {output_file} fájlba.")
print(f"Összesen {checked_count} videót ellenőriztünk nyelv alapján.")
