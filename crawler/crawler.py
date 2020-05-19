from bs4 import BeautifulSoup
import requests
from os.path import exists, basename
import os


def find_img_search_url(search):
    # pic_num = int(input('number of pictures'))
    img_url = None

    r = requests.get(f'https://www.google.com/search?q={search}')
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        if link.get_text() in ['Изображения', 'Images']:
            img_url = link.get('href')

    img_url = f'https://www.google.com{img_url}'

    return img_url

def download_pictures(img_number, search):

    img_url = find_img_search_url(search)

    r = requests.get(img_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    img_folder = f'images_{search}'

    if not exists(img_folder):
        os.mkdir(img_folder)

    img_count = 0

    for link in soup.find_all('img'):
        if 'http' in link.get('src'):
            link_img = link.get('src')
            with open(f'{img_folder}/{basename(link_img)}', 'wb') as f:
                f.write(requests.get(link_img).content)
            img_count += 1
        print(f"dwonload img num{img_count}")

        if img_count >= img_number:
            break
