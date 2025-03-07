import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
 
TOKEN = "8054309658:AAEeNQf1GRlHgrAnxGcuHB8bnX8y2_Kngqk"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hey there! 💖 I'm your Quote Bot. Use /quote  to get a random quote!")

def get_quote(update: Update, context: CallbackContext) -> None:
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        quote = f"💬 {data['content']}\n-{data['author']}"
        update.message.reply_text(quote)
    except Exception as e:
        update.message.reply_text("Oops! Couldn't fetch a quote. Try again later.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", get_quote))

    updater.start_polling()
    updater.idel()