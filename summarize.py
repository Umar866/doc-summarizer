import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

with open(sys.argv[1], encoding="utf-8") as f:
    text = f.read()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=f"Summarize this document in one paragraph, then list the 5 most important points.\n\n{text}",
)

print(response.text)