import whisper
import tempfile
import os

model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as f:
        f.write(audio_bytes)
        tmp_path = f.name
    
    result = model.transcribe(tmp_path)
    os.unlink(tmp_path)
    return result["text"].strip()