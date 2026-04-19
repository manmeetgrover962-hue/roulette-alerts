from flask import Flask
import requests

app = Flask(__name__)

BOT_TOKEN = "PASTE_YOUR_TOKEN_HERE"
CHAT_ID = "PASTE_YOUR_CHAT_ID_HERE"

@app.route("/")
def home():
    return "Roulette system running"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

@app.route("/test")
def test():
    send_telegram("✅ System working")
    return "Sent"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
