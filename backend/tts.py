from gtts import gTTS
import tempfile
import os

def text_to_speech(text: str) -> bytes:
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tts.save(f.name)
        tmp_path = f.name

    with open(tmp_path, "rb") as f:
        audio_bytes = f.read()

    os.unlink(tmp_path)
    return audio_bytes
