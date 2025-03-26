# chatbot.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def get_bot_response(user_input, history=[]):
    history.append(user_input)
    history_str = "\n".join(history)
    inputs = tokenizer.encode_plus(history_str, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=60, repetition_penalty=1.2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
