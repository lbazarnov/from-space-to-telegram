import os
import requests
from argparse import ArgumentParser
from from_space_to_telegram.downloading import download_image
from from_space_to_telegram.downloading import get_file_extension


def fetch_spacex_launch_images(path, launch_id=None):
    '''Fetches SpaceX launch images'''
    if launch_id:
        spacex_launch_images_url = 'https://api.spacexdata.com/v5/launches/{launch_id}'  # noqa: E501
        response = requests.get(spacex_launch_images_url)
        response.raise_for_status()
        images_urls = response.json()['links']['flickr']['original']
    else:
        response = requests.get('https://api.spacexdata.com/v5/launches/')
        response.raise_for_status()
        launches_with_images = [
            launch for launch in response.json() if launch['links']['flickr']['original']]
        images_urls = launches_with_images[0]['links']['flickr']['original']
    for image_number, image_url in enumerate(images_urls):
        file_extension = get_file_extension(image_url)
        download_image(image_url, os.path.join(
            path, f'spacex{image_number}{file_extension}'))


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        '-id', dest='launch_id', default='', help='SpaceX launch ID'
    )
    arg_parser.add_argument(
        '-d', dest='path', default='',
        help='Path to directory where images should be stored')
    args = arg_parser.parse_args()
    fetch_spacex_launch_images(args.path, args.launch_id)


if __name__ == "__main__":
    main()
