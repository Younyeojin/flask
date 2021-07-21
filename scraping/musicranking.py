from bs4 import BeautifulSoup
import pandas as pd                                 # as pd : as(별칭) + 줄임말
import requests


class MusicRanking(object):
    domain = ''                                     # ' ' : String 타입
    query_string = ''
    html = ''
    headers = {'User-Agent':'Mozilla/5.0'}
    class_name = []                                 # [ ] : 클래스 여러개다~
    artists = []
    titles = []
    dict = {}
    df = None                                       # df : 행렬

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'Crawling HTML is {self.html}')

    def get_ranking(self):
        soup = BeautifulSoup(self.html, 'lxml')

    def insert_dict(self):
        # 방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]

        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'            # csv:파일명
        self.df.to_csv(path, sep=',', na_rep='NaN')  # sep:        NaN : Null


def print_menu(ls):
    t = ''
    for i, j in enumerate(ls):
        t += str(i) + ' - ' + j + '\t'
    return int(input(t))


def main():
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output', 'Print Dict',
                           'Dict to Dataframe', 'Dataframe to CSV'])
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=09'
            mr.set_html()
        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = 'dayTime=2021072016'
            mr.set_html()
        elif menu == 3:
            # mr.tag_name =
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_ranking()

        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass




if __name__ == '__main__':
    main()