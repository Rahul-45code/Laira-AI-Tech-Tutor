from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import ask_laira

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Laira backend is running"}

@app.post("/chat")
def chat(data: dict):
    user_message = data.get("message", "")

    if not user_message:
        return {"reply": "Please ask a Python question 😊"}

    try:
        ai_reply = ask_laira(user_message)
        return {"reply": ai_reply}
    except Exception as e:
        return {"reply": "⚠️ AI error. Please try again later."}
