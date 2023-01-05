import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
from from_space_to_telegram.downloading import download_image
from from_space_to_telegram.downloading import get_file_extension
from from_space_to_telegram.scripts.fetch_spacex_images import fetch_spacex_launch_images  # noqa: E501


def fetch_nasa_apod(api_key, path):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,
               'count': 30}
    response = requests.get(url=nasa_url, params=payload)
    response.raise_for_status()
    image_urls = []
    for apod in response.json():
        if apod['media_type'] == 'video':
            pass
        image_urls.append(apod['url'])
    for image_number, image_url in enumerate(image_urls):
        file_extension = get_file_extension(image_url)
        file_path = f'{path}/nasa_apod_{image_number}{file_extension}'
        download_image(image_url, file_path)


def fetch_nasa_epic_photos(api_key, path):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': api_key}
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    recent_epic_images = response.json()
    for epic_image in recent_epic_images:
        epic_image_name = epic_image['image']
        filename = f'{epic_image_name}.png'
        image_datetime = datetime.fromisoformat(epic_image['date'])
        image_date = image_datetime.strftime('%Y/%m/%d')
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{filename}'  # noqa: E501
        file_path = f'{path}/nasa_{filename}'
        download_image(image_url, file_path, params=payload)


def run_scripts():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_TOKEN']
    images_path = 'images'
    Path(f'{images_path}').mkdir(exist_ok=True)
    fetch_spacex_launch_images(images_path)
    fetch_nasa_apod(nasa_api_key, images_path)
    fetch_nasa_epic_photos(nasa_api_key, images_path)
