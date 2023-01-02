import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote

NUMBER_OF_NASA_PHOTOS = 35


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    splitted_url = os.path.splitext(urlsplit(url).path)
    file_extension = splitted_url[1]
    return file_extension


def fetch_spacex_last_launch(path):
    spacex_launch_images_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'  # noqa: E501
    response = requests.get(spacex_launch_images_url)
    response.raise_for_status()
    json_response = response.json()['links']['flickr']['original']
    for image_number, image_url in enumerate(json_response):
        file_extension = get_file_extension(image_url)
        file_path = f'{path}spacex{image_number}{file_extension}'
        download_image(image_url, file_path)


def fetch_nasa_apod(api_key, path):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,
               'count': 35}
    response = requests.get(url=nasa_url, params=payload)
    response.raise_for_status()
    image_urls = [apod['url'] for apod in response.json()]
    for image_number, image_url in enumerate(image_urls):
        file_extension = get_file_extension(image_url)
        file_path = f'{path}nasa_apod_{image_number}{file_extension}'
        download_image(image_url, file_path)


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_TOKEN']
    images_path = 'images/'
    Path(f'{images_path}').mkdir(exist_ok=True)
    fetch_spacex_last_launch(images_path)
    fetch_nasa_apod(nasa_api_key, images_path)


if __name__ == '__main__':
    main()
