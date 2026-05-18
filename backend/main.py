from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
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

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.post("/talk")
async def talk(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    
    # Speech to text
    user_text = transcribe_audio(audio_bytes)
    
    # LLM response
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": user_text}]
    )
    reply_text = response.choices[0].message.content
    
    # Text to speech
    audio_response = text_to_speech(reply_text)
    
    return Response(
        content=audio_response,
        media_type="audio/mpeg",
        headers={"X-Transcript": user_text, "X-Reply": reply_text}
    )

@app.get("/")
def root():
    return {"status": "Voice AI running"}