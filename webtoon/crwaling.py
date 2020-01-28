import requests
from bs4 import BeautifulSoup as bs

from webtoon.models import Webtoon


def main_crawling():
    html_text = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=mon').text
    soup = bs(html_text, 'html.parser')
    webtoon_list = soup.select('.list_area .thumb a')

    for count, webtoon in enumerate(webtoon_list, 1):
        Webtoon.objects.create(
            title=webtoon.attrs["title"],
            webtoon_url='https://comic.naver.com{}'.format(webtoon.attrs["href"]),
            thumb_src=webtoon.select_one('img').get('src'),

        )

    return 0
