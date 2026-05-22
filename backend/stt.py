import tempfile
import os
import subprocess
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    ext = filename.split(".")[-1]
    
    # Save original file
    with tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False) as f:
        f.write(audio_bytes)
        input_path = f.name

    # Convert to wav using ffmpeg
    output_path = input_path.replace(f".{ext}", ".wav")
    
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", input_path,
            "-ar", "16000", "-ac", "1",
            "-f", "wav", output_path
        ], check=True, capture_output=True)

        with open(output_path, "rb") as f:
            transcription = client.audio.transcriptions.create(
                file=("audio.wav", f, "audio/wav"),
                model="whisper-large-v3-turbo",
                language="en"
            )
        return transcription.text.strip()

    finally:
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)