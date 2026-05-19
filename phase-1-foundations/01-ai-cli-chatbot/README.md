# 🤖 01 — AI CLI Chatbot

A terminal-based AI chatbot built using Python and OpenAI API.

This project is the first step in the Generative AI Engineer Learning Path and introduces the fundamentals of:

- LLM API integration
- Prompt handling
- Streaming responses
- Environment variables
- Conversational AI systems

---

# 🎯 Project Goal

Build a chatbot that:

- Runs inside the terminal
- Accepts user prompts
- Sends prompts to an LLM
- Streams AI responses
- Maintains conversation history

---

# 🧠 Concepts You Will Learn

## Core AI Concepts

- What is an LLM?
- Prompt engineering basics
- Chat completion APIs
- Tokens and context

## Python Concepts

- Functions
- Loops
- Exception handling
- Modules
- File structure

## API Concepts

- HTTP requests
- API keys
- JSON responses
- Streaming responses

## Development Skills

- Virtual environments
- Environment variables
- Git & GitHub basics

---

# 🛠 Tech Stack

| Area                   | Technology      |
|------------------------|-----------------|
| Language               | Python          |
| AI API                 | OpenAI API      |
| Environment Management | python-dotenv   |
| Terminal Styling       | Rich (Optional) |

---

# 📂 Project Structure

```txt
01-ai-cli-chatbot/
│
├── app/
│   ├── main.py
│   ├── chatbot.py
│   ├── prompts.py
│   ├── config.py
│   └── utils.py
│
├── conversations/
│   └── chat_history.json
│
├── tests/
│   └── test_chatbot.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📁 Folder Explanation

## `app/`

Contains the main application code.

### `main.py`

Application entry point.

### `chatbot.py`

Handles OpenAI API interaction.

### `prompts.py`

Stores reusable system prompts.

### `config.py`

Loads environment variables and settings.

### `utils.py`

Helper functions.

---

## `conversations/`

Stores conversation history locally.

---

## `tests/`

Unit tests for chatbot functionality.

---

# ⚙️ Features

## ✅ Basic Features

- Terminal-based chatbot
- AI responses
- Conversation memory
- Exit command

## 🚀 Advanced Features (Later)

- Streaming responses
- Multiple chat sessions
- Chat history saving
- Markdown rendering
- Voice support

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
```

## 2️⃣ Navigate to Project

```bash
cd 01-ai-cli-chatbot
```

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

```bash
python app/main.py
```

---

# 🧪 Example Chat

```txt
You: What is Generative AI?

AI:
Generative AI refers to AI systems capable of generating text,
images, code, audio, and other content using machine learning models.
```

---

# 📦 requirements.txt

```txt
openai
python-dotenv
rich
```

---

# 🚀 Future Improvements

#### Not Implementing currently but will explore later

## Version 2

- Streaming output
- Better UI
- Colored terminal

## Version 3

- Voice chatbot
- Local memory
- Multiple models
- Tool calling

---

# 🏆 Learning Outcome

After completing this project, you will understand:

- How to call LLM APIs
- How chatbots work
- API authentication
- Prompt-response workflow
- Basic AI application architecture

This project builds the foundation for:

- AI assistants
- RAG systems
- AI agents
- Production AI apps

---

# ⭐ Best Practices

✅ Uses environment variables  
✅ Wrote modular code  
✅ Added comments  
✅ Handled API errors properly  
✅ Saved conversation history

---

# 📚 Recommended Resources

## OpenAI API Docs

https://platform.openai.com/docs/

## Python Documentation

https://docs.python.org/3/

## FastAPI

https://fastapi.tiangolo.com/

---