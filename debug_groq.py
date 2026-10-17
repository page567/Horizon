import os
import httpx

key = os.environ.get("GROQ_API_KEY", "")
print("key present:", bool(key), "len:", len(key))
h = {"Authorization": "Bearer " + key}

r = httpx.get("https://api.groq.com/openai/v1/models", headers=h, timeout=30)
print("MODELS status:", r.status_code)
try:
    data = r.json()
    ids = [m.get("id") for m in data.get("data", [])]
    print("MODEL IDS:", ids)
except Exception:
    print("MODELS body:", r.text[:800])

for model in ["llama-3.3-70b-versatile", "openai/gpt-oss-120b", "llama-3.1-8b-instant"]:
    try:
        r = httpx.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={**h, "Content-Type": "application/json"},
            json={"model": model, "messages": [{"role": "user", "content": "Say OK"}], "max_tokens": 5},
            timeout=30,
        )
        print("CHAT", model, "status:", r.status_code, "body:", r.text[:600])
    except Exception as e:
        print("CHAT", model, "EXC:", repr(e))
