import fetch
import clean
import summarize
import re
from youtube_transcript_api import NoTranscriptFound, VideoUnavailable


def extract_video_id(url: str) -> str | None:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None


link = input("Enter URL of youtube video: ").strip()

video_id = extract_video_id(link)

if not video_id:
    print("❌ Invalid YouTube URL. Could not extract video ID.")
    exit(1)

try:
    fetch.fetch(video_id)
except NoTranscriptFound:
    print("❌ No transcript available for this video.")
    exit(1)
except VideoUnavailable:
    print("❌ Video is unavailable or private.")
    exit(1)
except Exception as e:
    print(f"❌ Failed while fetching transcript: {e}")
    exit(1)

try:
    clean.clean()
except Exception as e:
    print(f"❌ Error during cleaning step: {e}")
    exit(1)

try:
    summarize.summary()
except Exception as e:
    print(f"❌ Error during summarization: {e}")
    exit(1)

try:
    with open("summary.txt", "r") as fp:
        print("\n✅ Summary:\n")
        print(fp.read())
except FileNotFoundError:
    print("❌ Summary file not found. Summarization may have failed.")
