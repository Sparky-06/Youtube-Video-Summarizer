import re

def clean():
    # read no-use words once
    with open("noUseWords.txt", "r") as jp:
        no_use_words = [w.strip() for w in jp if w.strip()]

    # build regex pattern
    pattern = r'(?i)\b(' + '|'.join(map(re.escape, no_use_words)) + r')\b[.,]?'

    regex = re.compile(pattern, re.IGNORECASE)

    with open("fetch_transcript.txt", "r") as fp, open("clean.txt", "w") as cl:
        for line in fp:
            cleaned = regex.sub('', line)
            cleaned = re.sub(r'\s+', ' ', cleaned).strip()
            cl.write(cleaned + '\n')
