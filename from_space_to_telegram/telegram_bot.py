import os
import telegram
from dotenv import load_dotenv
from random import shuffle
from time import sleep
from argparse import ArgumentParser


def send_images_to_telegram(api_token, channel_id, images_directory, delay):
    '''Sends images to Telegram channel'''
    bot = telegram.Bot(token=api_token)
    images = []
    path_to_directory = os.path.join(os.getcwd(), images_directory)
    for subdirectory in os.walk(path_to_directory):
        base, _, files = subdirectory
        paths = [os.path.join(base, file) for file in files]
        images.extend(paths)
    while True:
        for image in images:
            with open(image, 'rb') as image:
                if os.path.getsize(image.name)/(1024**2) < 20:
                    bot.send_document(channel_id, document=image)
                    sleep(delay)
        shuffle(images)


def main():
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    channel_id = os.environ['CHANNEL_ID']
    path = 'images'
    arg_parse = ArgumentParser()
    arg_parse.add_argument(
        nargs='?',
        dest='pause_time',
        help='Time interval for posting photos to the channel in seconds',  # noqa: E501
        default=14400,
        type=int
    )
    args = arg_parse.parse_args()
    delay = args.pause_time
    try:
        send_images_to_telegram(
            telegram_api_token, channel_id, path, delay)
    except telegram.error.BadRequest as bad_request:
        print(bad_request)
    except telegram.error.Unauthorized as unauthorized_user:
        print(f'Oops! {unauthorized_user}. Looks like the Telegram API token '
              'you entered is incorrect or expired.'
              ' Please check it and try again.')


if __name__ == '__main__':
    main()
