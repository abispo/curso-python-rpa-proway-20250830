from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

import os
import datetime

load_dotenv()

class AutomacaoProwayBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(token=os.getenv("TELEGRAM_TOKEN"))

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Olá! Eu sou o bot telegram da turma RPA com Python! ({datetime.datetime.now()})")

if __name__ == "__main__":
    app = ApplicationBuilder().bot(AutomacaoProwayBot()).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
