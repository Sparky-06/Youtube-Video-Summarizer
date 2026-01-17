from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_api_key")
    )


def read_in_chunks(path, chunk_size=100):
    with open(path, "r") as fp:
        chunk = []
        for line in fp:
            chunk.append(line.rstrip("\n"))
            if len(chunk) == chunk_size:
                yield "\n".join(chunk)
                chunk = []
        if chunk:
            yield "\n".join(chunk)


def summary():
    output_summary = ""
    for text_to_summarize in read_in_chunks("clean.txt", 100):

        response = client.responses.create(
        model="gpt-5-nano",
        input=f"Summarize this: {text_to_summarize}. \nGive detailed summary only, no fillers, nothing.",
        store=True,
        )
        output_summary = output_summary + " " + response.output_text

    with open ("summary.txt", "w+") as fp:
        fp.write(output_summary)


summary()