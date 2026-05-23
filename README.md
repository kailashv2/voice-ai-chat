# 🎤 Voice AI

> Talk to it. It thinks. It talks back.

A voice-powered AI assistant built from scratch using open source tools.
No ChatGPT. No paid wrappers. Just raw code.

## 🚀 Live Demo

🌐 **Try it here:** https://huggingface.co/spaces/Kailashalgo/voice-ai-chat

Press and hold the mic button → speak → AI replies out loud.

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| 🎤 Speech to Text | Whisper Large V3 Turbo (via Groq API) |
| 🧠 AI Brain | LLaMA 3.3 70B (via Groq) |
| 🔊 Text to Speech | gTTS |
| ⚡ Backend | FastAPI + Python |
| 🌐 Frontend | Vanilla HTML/CSS/JS |
| 🐳 Container | Docker |
| ☁️ Hosting | HuggingFace Spaces |

## ⚙️ Setup Locally

### 1. Clone the repo
```bash
git clone https://github.com/kailashv2/voice-ai-chat.git
cd voice-ai-chat
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 4. Add your Groq API key
Create `.env` file in root:
```
GROQ_API_KEY=your_groq_key_here
```
Get your free key at: https://console.groq.com

### 5. Install ffmpeg
Download from: https://www.gyan.dev/ffmpeg/builds/
Add to PATH

### 6. Run the server
```bash
cd backend
uvicorn main:app --reload
```

### 7. Open the frontend
Open `frontend/index.html` in Chrome

## 🎯 How It Works

```
You speak → Whisper transcribes → LLaMA thinks → gTTS speaks
```

1. Browser records your voice
2. Audio sent to FastAPI backend
3. Groq Whisper transcribes speech to text
4. LLaMA 3.3 70B generates a reply
5. gTTS converts reply to audio
6. Browser plays the audio back

## 🐳 Docker

```bash
docker build -t voice-ai-chat .
docker run -p 7860:7860 -e GROQ_API_KEY=your_key voice-ai-chat
```

## 📁 Project Structure

```
voice-ai-chat/
├── backend/
│   ├── main.py            ← FastAPI server
│   ├── stt.py             ← Speech to text (Groq Whisper)
│   ├── tts.py             ← Text to speech (gTTS)
│   └── requirements.txt   ← Python dependencies
├── frontend/
│   └── index.html         ← UI
├── Dockerfile             ← Docker deployment
├── .env.example           ← Environment variables template
├── .gitignore
└── README.md
```

## 🆓 Cost

Completely free.
- Groq API: Free tier
- Whisper: Free via Groq
- gTTS: Free
- Hosting: HuggingFace Spaces (free)

## 🌐 Deployment

Deployed on HuggingFace Spaces with Docker.

Live URL: https://huggingface.co/spaces/Kailashalgo/voice-ai-chat

## 👨‍💻 Built By

Kailash 

Follow the journey on X: @kailashv2

⭐ Star this repo if you found it useful!
