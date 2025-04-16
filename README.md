# 🤖 Smita's Chatbot

A friendly, responsive AI-powered chatbot built using **Flask**, **HTML**, **CSS**, and **JavaScript** — designed with a mobile-style layout and user-friendly UX. Features avatars, typing animations, and send button states for feedback.

---

## ✨ Features

- 💬 Mobile-style chat interface
- 🧑‍💻 Avatars for both user and bot
- ⏳ Animated “Bot is typing...” indicator
- 🔘 Send button feedback (disabled while sending)
- 🌈 Clean, modern visual design
- 🧠 Optional LLM integration (e.g., Hugging Face’s Mistral-7B)
- ☁️ Deployable on Replit or Render

---

## 📂 Project Structure

chatbot/ ├── app.py ├── requirements.txt ├── .replit ├── /templates │ └── index.html ├── /static │ ├── style.css │ ├── script.js │ ├── bot-avatar.png │ └── user-avatar.png └── README.md

yaml
Copy
Edit

---

## 🚀 How to Run Locally

1. Clone the repo
2. Install dependencies
3. Run the Flask app

```bash
git clone https://github.com/SmitaKas/chatbot.git
cd chatbot
pip install -r requirements.txt
python app.py

Then open http://localhost:5000 in your browser.

