import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

ai_client = genai.Client(api_key=GEMINI_API_KEY)
app = Client(":AIBot:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command(["start", "help"]))
async def start_cmd(_, message: Message):
    await message.reply_text("Hello! Main ek AI ChatBot hoon. Mujhse koi bhi sawal poocho ya baat karo!")

@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def ai_chat(_, message: Message):
    await app.send_chat_action(message.chat.id, "typing")
    try:
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message.text,
        )
        await message.reply_text(response.text)
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text("Sorry, kuch dikkat aa gayi reply dene me.")

if __name__ == "__main__":
    app.run()
