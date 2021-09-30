import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import maya
from core.modules.news._news import create_news
from core.static.news import Type
import pprint


class CrawlerCoinMarketCal:
    base_url = "https://coinmarketcal.com/en/"

    def __init__(self, coin_dicts):
        self.coin_dicts = coin_dicts

    def get_coin_news_list(self):
        url_list = self.get_url_list()
        coin_news_return_list = []
        coin_id_list = []
        for url in url_list:
            coin_ticker_list, coin_news_list = self.do_crawl(url)
            for coin_ticker, coin_news in zip(coin_ticker_list, coin_news_list):
                if coin_ticker in self.coin_dicts.keys():
                    coin_news_return_list.append(coin_news)
                    coin_id_list.append(self.coin_dicts[coin_ticker])
        return coin_news_return_list, coin_id_list

    def get_url_list(self):
        html = urlopen(self.base_url)
        soup = BeautifulSoup(html, "html.parser")
        page_data = soup.select("a[class='page-link rounded']").pop()
        max_page = re.findall("\d+", str(page_data)).pop()
        max_page = int(max_page)
        url_list = []
        for i in range(1, max_page + 1):
            url_list.append("https://coinmarketcal.com/en/" + "?page=" + str(i))
        return url_list

    @staticmethod
    def do_crawl(url):
        html = urlopen(url)

        # 사이트에 문제가 있으면 함수 종료
        if html.status != 200:
            return
        soup = BeautifulSoup(html, "html.parser")

        title_data = soup.select(
            "article.col-xl-3.col-lg-4.col-md-6.py-3 > div.card.text-center > div.card__body > a.link-detail > h5.card__title.mb-0.ellipsis")
        link_data = soup.select(
            "article.col-xl-3.col-lg-4.col-md-6.py-3 > div.card.text-center > div.card__body > a.link-detail")
        upload_date_data = soup.select("div.position-relative > p.added-date")
        release_date_data = soup.select("h5[class = 'card__date mt-0']")
        name_data = soup.select(
            "article.col-xl-3.col-lg-4.col-md-6.py-3 > div.card.text-center > div.card__body > h5.card__coins > a.link-detail")

        min_len = min(len(name_data), len(release_date_data), len(title_data), len(upload_date_data),
                      len(release_date_data))
        coin_news_list = []
        coin_ticker_list = []
        for i in range(0, min_len):
            # title
            title = str(title_data[i].string)
            # link
            link = str(link_data[i])
            link = link[link.find('href="') + 6: link.find('" title')]
            link = "https://coinmarketcal.com" + link

            # source
            source = 'coinmarketcal'

            # upload_date
            upload_date = str(upload_date_data[i].string).replace('Added', '')
            upload_date = maya.parse(upload_date).datetime()

            # release_date
            release_date = str(release_date_data[i].string).replace('(or earlier)', '')
            release_date = maya.parse(release_date).datetime()

            # name
            name = ' '.join(name_data[i].string.split())
            name = [name[0: name.find('(') - 1], name[name.find('(') + 1: name.find(')')]]

            coin_news = create_news(Type.COIN_MARKET_CAL, title, source, link, upload_date, release_date)
            coin_ticker_list.append(name[1])
            coin_news_list.append(coin_news)
        return coin_ticker_list, coin_news_list
