import requests
from dotenv import load_dotenv
from from_space_to_telegram.downloading import download_image
from from_space_to_telegram.downloading import get_file_extension


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


def main():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_TOKEN']
    fetch_nasa_apod(nasa_api_key, 'images')
