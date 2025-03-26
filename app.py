from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

# Load model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    inputs = tokenizer(user_message, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=60, repetition_penalty=1.2)
    bot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, port=3000)  # ← changed port to 8000
