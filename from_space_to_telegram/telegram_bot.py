import os
import telegram
from dotenv import load_dotenv

load_dotenv()
telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
channel_id = os.environ['CHANNEL_ID']
bot = telegram.Bot(token=telegram_api_token)
bot.send_message(text='Hello', chat_id=channel_id)
