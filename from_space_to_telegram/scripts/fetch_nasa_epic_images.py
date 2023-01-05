import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from argparse import ArgumentParser
from from_space_to_telegram.downloading import download_image


def fetch_nasa_epic(api_key, path):
    '''Fetches NASA EPIC images'''
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': api_key}
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    for epic_image in response.json():
        epic_image_name = epic_image['image']
        filename = f'{epic_image_name}.png'
        image_datetime = datetime.fromisoformat(epic_image['date'])
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{filename}'  # noqa: E501
        download_image(image_url, os.path.join(
            path, f'nasa_{filename}'), params=payload)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_TOKEN']
    arg_parse = ArgumentParser()
    arg_parse.add_argument(
        '-d',
        dest='path',
        default=os.getcwd(),
        help='Path to directory where images should be stored'
    )
    args = arg_parse.parse_args()
    fetch_nasa_epic(nasa_api_key, args.path)


if __name__ == '__main__':
    main()
