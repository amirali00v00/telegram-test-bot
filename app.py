import os
import requests

from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ["BOT_TOKEN"]

TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"


@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json

    message = update.get("message")

    if message:
        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            requests.post(
                f"{TELEGRAM_URL}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "سلام امیرعلی 👋😎"
                }
            )

    return "OK"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
