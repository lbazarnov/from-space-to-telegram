import requests
from pathlib import Path


def get_images_urls_list(url):
    response = requests.get(url)
    response.raise_for_status()
    json_response = response.json()
    spacex_launch_images_urls = json_response['links']['flickr']['original']
    return spacex_launch_images_urls


def download_image(urls, path):
    for image_number, image_url in enumerate(urls):
        response = requests.get(image_url)
        response.raise_for_status()
        filename = f'{path}spacex{image_number}.jpg'
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    images_path = 'images/'
    Path(f'{images_path}').mkdir(exist_ok=True)
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    images_urls = get_images_urls_list(spacex_url)
    download_image(images_urls, images_path)


if __name__ == '__main__':
    main()
