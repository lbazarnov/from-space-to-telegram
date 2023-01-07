import os
import requests
from dotenv import load_dotenv
from argparse import ArgumentParser
from from_space_to_telegram.downloading import download_image
from from_space_to_telegram.downloading import get_file_extension


def fetch_nasa_apod(api_key, path):
    '''Fetches 30 random NASA Astronomy Pictures of the Day'''
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,
               'count': 30}
    response = requests.get(url=nasa_url, params=payload)
    response.raise_for_status()
    image_urls = []
    for apod in response.json():
        if apod['media_type'] != 'video':
            image_urls.append(apod['url'])
    for image_number, image_url in enumerate(image_urls):
        file_extension = get_file_extension(image_url)
        download_image(image_url, os.path.join(
            path, f'nasa_apod_{image_number}{file_extension}'))


def main():
    load_dotenv()
    nasa_api_token = os.environ['NASA_API_TOKEN']
    arg_parse = ArgumentParser()
    arg_parse.add_argument(
        '-d',
        dest='path',
        default=os.getcwd(),
        help='Path to directory where images should be stored')
    args = arg_parse.parse_args()
    fetch_nasa_apod(nasa_api_token, args.path)


if __name__ == '__main__':
    main()
