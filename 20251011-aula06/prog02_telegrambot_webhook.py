from fastapi import FastAPI, Request
from telegram import Bot
from telegram.ext.filters import Text

from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

import uvicorn

load_dotenv()

api_app = FastAPI()

class AutomacaoProwayBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(token=os.getenv("TELEGRAM_TOKEN"))


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_name = update.message.from_user.first_name

    response = f"Olá {user_name}. Você escreveu '{user_text}'."

    await update.message.reply_text(response)

bot_app = ApplicationBuilder().bot(AutomacaoProwayBot()).build()
bot_app.add_handler(MessageHandler(filters.TEXT, echo))

api_app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.process_update(update)
    return {"status": "OK"}

@api_app.on_event("startup")
async def startup():
    await bot_app.bot.set_webhook(os.getenv("WEBHOOK_URL"))

if __name__ == "__main__":
    uvicorn.run(api_app, host="0.0.0.0", port=8000)