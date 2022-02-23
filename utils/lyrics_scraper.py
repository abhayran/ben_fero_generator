import requests
import json
from bs4 import BeautifulSoup
from typing import List


def get_soup_instance(url: str) -> BeautifulSoup:
    return BeautifulSoup(requests.get(url).content, parser='html.parser', features="lxml")


def check_if_page_empty(url: str) -> bool:
    alerts = get_soup_instance(url).find_all('div', attrs={'class': ['alert', 'alert-warning']})
    return len(alerts) == 1 and alerts[0].text == 'Sorry, your search returned no results. Try to compose less ' \
                                                  'restrictive search query or check spelling.'


def get_song_urls() -> List[str]:
    base_url = 'https://search.azlyrics.com/search.php?q=ben+fero&w=songs&p='
    urls = []
    page_number = 1
    while not check_if_page_empty(f'{base_url}{page_number}'):
        urls.extend([link['href'] for link in get_soup_instance(f'{base_url}{page_number}').find_all('a')
                     if 'azlyrics.com/lyrics' in link.attrs['href']])
        page_number += 1
    return urls


def get_start_idx(lyrics: List[str]) -> int:
    for idx, lyric in enumerate(lyrics):
        if '"' in lyric:
            return idx
    return 0


def get_end_idx(lyrics: List[str]) -> int:
    try:
        return lyrics.index(' Submit Corrections') + 1
    except ValueError:
        return len(lyrics)


def parse_song_lyrics(url: str) -> List[str]:
    lyrics = get_soup_instance(url).find_all('div', attrs={'class': ['container main-page']})
    lyrics = lyrics[0].text.strip().split('\n')
    return [item for item in lyrics[get_start_idx(lyrics):get_end_idx(lyrics)] if item]


def create_dataset(output_path: str):
    dataset = {url.split('/')[-1].replace('.html', ''): parse_song_lyrics(url) for url in get_song_urls()}
    with open(output_path, 'w') as json_file:
        json.dump(dataset, json_file)


if __name__ == '__main__':
    create_dataset('../dataset/lyrics.json')
