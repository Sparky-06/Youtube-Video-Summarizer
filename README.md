# YouTube Transcript Cleaner + Summarizer


### THIS IS STAGE 1 OF THE PROJECT
Later stages will have standalone model instead of openAI and more features into it.

## A small Python project that:
1. Fetches a YouTube video transcript
2. Cleans out filler / “no-use” words
3. Summarizes the cleaned transcript using the OpenAI API
---

## Features

- ✅ Fetch YouTube transcripts by video ID
- ✅ Remove filler words like `uh`, `umm`, `you know`, etc.
- ✅ Save intermediate outputs (`fetch_transcript.txt`, `clean.txt`)
- ✅ Generate a final combined summary (`summary.txt`)
- ✅ Processes the transcript in chunks to avoid sending everything at once

---

## Project Files

- **`fetch.py`**  
  Fetches transcript text from YouTube and writes it to `fetch_transcript.txt`

- **`clean.py`**  
  Removes words listed in `noUseWords.txt` and writes output to `clean.txt`

- **`summarize.py`**  
  Summarizes `clean.txt` using OpenAI and writes to `summary.txt`

- **`noUseWords.txt`**  
  List of filler words/phrases to remove

- **`requirements.txt`**  
  Python dependencies

---

## Installation

### 1) Clone / download the project
```bash
git clone https://github.com/Sparky-06/Youtube-Video-Summarizer.git
cd Youtube-Video-Summarizer
```

### Create and activate virtual enviorment (recommanded)
```bash
python -m venv .venv
```

#Windows
```bash
.venv\Scripts\activate
```

#macOS/Linux
```bash
source .venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirments.txt
```
###Setup OPEN AI key
create a .env file in the project root:
``` env
OPENAI_api_key=your_openai_api_key_here
```

### Usage
- Run the main.py file
- Enter the Youtube video URL
- It will create txt files, if not there (fetch_transcript.txt, clean.txt, summary.txt)
- Returns the summaey as output as well as in summary.txt

### Output Files
- fetch_transcript.txt	-> Raw transcript fetched from YouTube
- clean.txt	Transcript -> cleaned of filler words
- summary.txt	Final -> combined summary

### Customizing filter words
Edit noUseWords.txt and add/remove entries (1 per line), for example:
```txt
uh
umm
you know
it's like
```

### Notes / Limitations
- Transcript fetching requires that the video has transcripts available.
- Some videos may block transcript access or not provide transcripts.
- Summarization uses model: gpt-5-nano
- Summarize.py chunks the transcript in batches of 100 lines to avoid huge single requests.


### License
MIT
