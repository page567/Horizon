import os
import traceback

import httpx
from google import genai

key = os.environ["GOOGLE_API_KEY"]

print("=== RAW HTTP ===")
try:
    r = httpx.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": "Say OK"}]}]},
        timeout=60,
    )
    print("STATUS:", r.status_code)
    print("BODY:", r.text[:1500])
except Exception:
    traceback.print_exc()

print("=== GENAI SDK ===")
try:
    client = genai.Client(api_key=key)
    resp = client.models.generate_content(model="gemini-2.5-flash", contents="Say OK")
    print("TEXT:", resp.text)
except Exception:
    traceback.print_exc()
