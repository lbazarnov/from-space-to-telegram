import requests
import os
from urllib.parse import urlsplit


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    splitted_url = os.path.splitext(urlsplit(url).path)
    file_extension = splitted_url[1]
    return file_extension
