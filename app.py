from flask import Flask, render_template, request, jsonify
import requests
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Hugging Face API config
HF_TOKEN = os.getenv("HF_TOKEN")  # token stored in .env
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# Store the user's name temporarily during session
user_name = None

# Simple name extractor
def extract_name(text):
    match = re.search(r"(?:my name is|i'm|i am)\s+([A-Z][a-z]+)", text, re.IGNORECASE)
    if match:
        name = match.group(1).strip().capitalize()
        if name.lower() not in ["bored", "sad", "tired", "hungry"]:
            return name
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global user_name
    user_message = request.json["message"]

    # Try to extract and store name
    name_found = extract_name(user_message)
    if name_found:
        user_name = name_found

    # Prefix prompt for better personalization
    if user_name:
        chat_prefix = f"You are chatting with someone named {user_name}. Always call them by their name."
    else:
        chat_prefix = "You are chatting with a user. Be polite and helpful."

    prompt = f"[INST] {chat_prefix} {user_message} [/INST]"

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            bot_reply = result[0]["generated_text"].split("[/INST]")[-1].strip()
        else:
            bot_reply = "Sorry, I couldn't understand that."

    except Exception as e:
        print("Error:", e)
        bot_reply = "Sorry, something went wrong."

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=3002)