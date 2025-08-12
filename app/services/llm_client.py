import os, requests

PROVIDER = os.getenv("MODEL_PROVIDER", "together").lower()

def generate(prompt: str, max_tokens: int = 256) -> str:
    if PROVIDER == "together":
        key = os.getenv("TOGETHER_API_KEY")
        if not key:
            return f"[MOCKED] LLM response for: {prompt[:120]}..."
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}"}
        payload = {
            "model": "meta-llama/Meta-Llama-3-8B-Instruct-Turbo",
            "messages": [{"role":"system","content":"You are a supply chain copilot."},
                         {"role":"user","content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.2
        }
        r = requests.post(url, json=payload, headers=headers, timeout=60)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    elif PROVIDER == "fireworks":
        key = os.getenv("FIREWORKS_API_KEY")
        if not key:
            return f"[MOCKED] LLM response for: {prompt[:120]}..."
        url = "https://api.fireworks.ai/inference/v1/chat/completions"
        headers = {"Authorization": f"Bearer {key}"}
        payload = {
            "model": "accounts/fireworks/models/llama-v3-8b-instruct",
            "messages": [{"role":"system","content":"You are a supply chain copilot."},
                         {"role":"user","content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.2
        }
        r = requests.post(url, json=payload, headers=headers, timeout=60)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"[MOCKED] Unknown provider; prompt: {prompt[:120]}..."
