import urllib.parse
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, FileResponse
from fastapi.staticfiles import StaticFiles
from groq import Groq
from dotenv import load_dotenv
from stt import transcribe_audio
from tts import text_to_speech
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a fast voice assistant.
Rules:
- Reply in MAX 2-3 short sentences
- Never use bullet points or markdown
- Speak naturally like a human
- Be direct and concise
- Reply in the same language the user speaks"""

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/talk")
async def talk(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    filename = audio.filename or "audio.webm"

    user_text = transcribe_audio(audio_bytes, filename)
    print(f"User said: {user_text}")

    if not user_text:
        return Response(
            content=b"",
            media_type="audio/mpeg",
            headers={
                "X-Transcript": "",
                "X-Reply": "I didn't catch that",
                "Access-Control-Expose-Headers": "X-Transcript, X-Reply"
            }
        )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        max_tokens=100
    )
    reply_text = response.choices[0].message.content
    print(f"AI reply: {reply_text}")

    audio_response = text_to_speech(reply_text)

    return Response(
        content=audio_response,
        media_type="audio/mpeg",
        headers={
            "X-Transcript": urllib.parse.quote(user_text),
            "X-Reply": urllib.parse.quote(reply_text),
            "Access-Control-Expose-Headers": "X-Transcript, X-Reply"
        }
    )
