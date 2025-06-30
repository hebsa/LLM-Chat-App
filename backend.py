from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow Streamlit to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        user_input = body.get("message", "")

        # Call Ollama and capture the full streamed response
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": user_input, "stream": False}
        )
        response.raise_for_status()

        data = response.json()
        reply = data.get("response", "No reply found.")

        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Error: {str(e)}"}
