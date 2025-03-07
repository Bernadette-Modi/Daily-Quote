import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
 
TOKEN = "8054309658:AAEeNQf1GRlHgrAnxGcuHB8bnX8y2_Kngqk"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)