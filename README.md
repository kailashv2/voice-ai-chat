# 🎤 Voice AI

> Talk to it. It thinks. It talks back.

A voice-powered AI assistant built from scratch using open source tools.
No ChatGPT. No paid wrappers. Just raw code.

## 🚀 Demo

Press and hold the mic button → speak → AI replies out loud.

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| 🎤 Speech to Text | Whisper (via Groq API) |
| 🧠 AI Brain | LLaMA 3.3 70B (via Groq) |
| 🔊 Text to Speech | gTTS |
| ⚡ Backend | FastAPI + Python |
| 🌐 Frontend | Vanilla HTML/CSS/JS |

## ⚙️ Setup

### 1. Clone the repo
git clone https://github.com/kailashv2/voice-ai-chat.git
cd voice-ai-chat

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
cd backend
pip install -r requirements.txt

### 4. Add your Groq API key
Create .env file in root:
GROQ_API_KEY=your_groq_key_here
Get your free key at: https://console.groq.com

### 5. Install ffmpeg
Download from: https://www.gyan.dev/ffmpeg/builds/
Add to PATH

### 6. Run the server
cd backend
uvicorn main:app --reload

### 7. Open the frontend
Open frontend/index.html in Chrome

## 🎯 How It Works

You speak → Whisper transcribes → LLaMA thinks → gTTS speaks

1. Browser records your voice
2. Audio sent to FastAPI backend
3. Groq Whisper transcribes speech to text
4. LLaMA 3.3 70B generates a reply
5. gTTS converts reply to audio
6. Browser plays the audio back

## 📁 Project Structure

voice-ai-chat/
├── backend/
│   ├── main.py        ← FastAPI server
│   ├── stt.py         ← Speech to text (Groq Whisper)
│   ├── tts.py         ← Text to speech (gTTS)
│   └── requirements.txt
├── frontend/
│   └── index.html     ← UI
├── .env               ← API keys (not committed)
└── README.md

## 🆓 Cost

Completely free.
- Groq API: Free tier
- Whisper: Free via Groq
- gTTS: Free
- Hosting: Your machine / HuggingFace Spaces

## 🌐 Deploy

Coming soon on HuggingFace Spaces.

## 👨‍💻 Built By

Kailash

⭐ Star this repo if you found it useful!
