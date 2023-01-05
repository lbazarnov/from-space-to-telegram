import os
import telegram
from dotenv import load_dotenv

load_dotenv()
telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
bot = telegram.Bot(token=telegram_api_token)
print(bot.get_me())
