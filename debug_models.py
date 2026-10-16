import os
import traceback

import httpx
from openai import OpenAI

token = os.environ["GH_MODELS_TOKEN"]
base = "https://models.github.ai/inference"

print("=== RAW HTTP ===")
try:
    r = httpx.post(
        base + "/chat/completions",
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": "Return JSON only with keys score, reason, summary, tags. Item: Major AI chip announcement."}],
            "response_format": {"type": "json_object"},
            "max_tokens": 200,
        },
        timeout=60,
    )
    print("STATUS:", r.status_code)
    print("BODY:", r.text[:1500])
except Exception:
    traceback.print_exc()

print("=== OPENAI SDK ===")
try:
    client = OpenAI(api_key=token, base_url=base)
    resp = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": "Return JSON only with keys score, reason, summary, tags. Item: Major AI chip announcement."}],
        response_format={"type": "json_object"},
        max_tokens=200,
    )
    print("REPR:", repr(resp)[:1500])
    print("CONTENT TYPE:", type(resp.choices[0].message.content))
    print("CONTENT:", repr(resp.choices[0].message.content)[:500])
except Exception:
    traceback.print_exc()
