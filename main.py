import datetime

import requests
from bs4 import BeautifulSoup
import dataclasses


@dataclasses.dataclass
class News:
    title: str
    full_text: str
    news_date: datetime.datetime
    author: str


class LigaTek:
    def __init__(self):
        self.ses = requests.Session()

    def __iter__(self):
        paige = self.ses.get('https://tech.liga.net/technology')
        self.soup = BeautifulSoup(paige.content, 'html.parser')
        self.inx = -1
        return self

    def load_news(self, link) -> News:
        pass

    def __next__(self) -> News:
        news_ul = self.soup.find('ul', class_='news')
        if news_ul is None:
            raise StopIteration
        a = news_ul.find_all('a')
        my_links = []
        for i in a:
            if 'href' in i.attrs and i.attrs['href']:
                my_links.append(i.attrs['href'])
        self.inx += 1
        if self.inx < len(my_links):
            return self.load_news(my_links[self.inx])
        raise StopIteration


if __name__ == '__main__':
    for link in LigaTek():
        print(link)
