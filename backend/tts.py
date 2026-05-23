from gtts import gTTS
import tempfile
import os
from io import BytesIO

def text_to_speech(text: str) -> bytes:

    try:
        from langdetect import detect
        lang = detect(text)
    except:
        lang = "en"

    lang_map = {
        "hi": "hi",  # Hindi
        "ur": "ur",  # Urdu  
        "ta": "ta",  # Tamil
        "te": "te",  # Telugu
        "bn": "bn",  # Bengali
        "mr": "mr",  # Marathi
        "gu": "gu",  # Gujarati
        "en": "en",  # English
    }

    tts_lang = lang_map.get(lang, "en")

    tts = gTTS(text=text, lang=tts_lang, slow=False)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tts.save(f.name)
        tmp_path = f.name

    with open(tmp_path, "rb") as f:
        audio_bytes = f.read()

    os.unlink(tmp_path)
    return audio_bytes
