from pyrogram import Client, filters
import os

api_id = int(os.getenv("23810708"))
api_hash = os.getenv("975a25803061985218a636cc17f955d5")
bot_token = os.getenv("8050458245:AAHNHo0QZ_EuPQa9PYXtjWPZmG4VQujwGKU")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("👋 مرحبًا! أنا بوت تيليجرام أعمل على Render.")

app.run()