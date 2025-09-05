# Ollama Local Chatbot

This is a simple Python chatbot that you can integrate into your projects. It runs **locally** using [Ollama](https://ollama.ai) and the **Gemma 2B** language model.  
No API keys or internet connection are required once the model is downloaded.

---

## Requirements

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.ai) (local LLM runner)

---

## Installation

1. ### Clone this repository

   ```bash
   git clone https://github.com/ndubuisi-ugwuja/chatbot.git
   cd bot
   ```

2. ### Install Python dependencies

   ```bash
   pip install ollama
   ```

3. ### Install Ollama

   \*Linux/macOS

   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

   \*Windows (WSL2 required)
   Follow the guide: [Ollama on Windows](https://ollama.ai/download/windows?utm_source=chatgpt.com)

4. ### Pull the Gemma 2B model

   ```bash
   ollama pull gemma:2b
   ```

## Run ollama server locally

\*Keep it running

```bash
ollama serve
```

## 🚀 Run the chatbot

\*Open another terminal

```bash
python chatbot.py
```

You can now chat with the bot on your terminal:

```bash
Chatbot🤖 (Gemma-2B) (type 'exit' to quit)

You: Hello!
Bot: Hi there! How can I help you today?
```

📝 Notes

The gemma 2b Model is large (1.6–2 GB or more), so the first pull may take some time.

All processing happens locally on your machine. No data leaves your computer.
