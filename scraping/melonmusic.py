from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse

class MelonMusic(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0'}

    def scrap(self):
        x = urllib.request.Request(self.url, headers=self.headers)
        soup = BeautifulSoup(urllib.request.urlopen(x).read(), 'lxml')
        _ = 0
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        print(f'List size is {len(artists)}')
        for i, j in zip(artists, titles):
            _ += 1
            print(f"Rank {str(_)} Artist: {i.find('a').text}, Title: {j.find('a').text}")


if __name__ == '__main__':
    MelonMusic(f'https://www.melon.com/chart/index.htm?dayTime=2021072016').scrap()