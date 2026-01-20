import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b"

def ask_laira(user_message: str) -> str:
    payload = {
    "model": MODEL_NAME,
    "prompt": f"""
You are Laira, a patient and friendly Python tutor for absolute beginners.

Teaching rules:
- Explain in very simple language
- Use small examples
- If the question is basic, explain slowly
- If code is needed, show short code
- Encourage the learner

Student question:
{user_message}

Laira's answer:
""",
    "stream": False
}


    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print("OLLAMA ERROR:", e)
        return "⚠️ Local AI error"
