import os
from pathlib import Path
from dotenv import load_dotenv
from from_space_to_telegram.scripts.fetch_spacex_images import fetch_spacex_launch_images  # noqa: E501
from from_space_to_telegram.scripts.fetch_nasa_apod_images import fetch_nasa_apod  # noqa: E501
from from_space_to_telegram.scripts.fetch_nasa_epic_images import fetch_nasa_epic  # noqa: E501


def main():
    load_dotenv()
    nasa_api_token = os.environ['NASA_API_TOKEN']
    images_path = 'images'
    Path(f'{images_path}').mkdir(exist_ok=True)
    fetch_spacex_launch_images(images_path)
    fetch_nasa_apod(nasa_api_token, images_path)
    fetch_nasa_epic(nasa_api_token, images_path)


if __name__ == '__main__':
    main()
