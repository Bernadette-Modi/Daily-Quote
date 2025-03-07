import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8054309658:AAEeNQf1GRlHgrAnxGcuHB8bnX8y2_Kngqk"

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey there! 💖 I'm your Quote Bot. Use /quote to get a random quote!")

# Function to get a quote
def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f"💡 {data['content']} — {data['author']}"
    else:
        return "Sorry, I couldn't fetch a quote at the moment. Try again later."

# Quote command
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote_text = get_quote()
    await update.message.reply_text(quote_text)

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quote", quote))

    app.run_polling()

if __name__ == "__main__":
    main()
