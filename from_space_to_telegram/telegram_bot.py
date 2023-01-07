import os
import time
import telegram
from dotenv import load_dotenv


def send_images_to_telegram(api_token, channel_id, path):
    bot = telegram.Bot(token=api_token)
    root, dirs, files = os.walk(path)
    for image in files:
        bot.send_photo(chat_id=channel_id, photo=open(f'{image}', 'rb'))


def main():
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    channel_id = os.environ['CHANNEL_ID']
    path = 'images'
    send_images_to_telegram(telegram_api_token, channel_id, path)


if __name__ == '__main__':
    main()
