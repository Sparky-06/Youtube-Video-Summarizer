from youtube_transcript_api import YouTubeTranscriptApi

ytapi = YouTubeTranscriptApi()

def fetch(VIDEO_ID):

    text = ytapi.fetch(VIDEO_ID)

    #print(text)

    with open ("fetch_transcript.txt","w+") as fp:
        for i in text:
            #print(i.text[1:])
            if i.text[0] == '>':
                fp.write(i.text[3:])
            else:
                fp.write(i.text)
            fp.write("\n")