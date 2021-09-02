from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import timedelta
import maya
from ._news import create_news


class CrawlerGoogle:
    @staticmethod
    def url_parser(coin: str):
        url = 'https://news.google.com/rss/search?q=' + coin + '+when:1d&hl=en-NG&gl=NG&ceid=NG:en'
        return url

    @staticmethod
    def do_crawl(url: str, coin_id_list, coin):
        response = urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        news_list = []
        item_list = soup.find_all('item')
        for item in item_list:
            description_data = item.find('description').string
            item_data = str(item)

            title = str(item.find('title').string)
            source = item_data
            source = source[source.find('<source'):source.find('</item>')]
            source = source[source.find('"/>') + 3:]
            link = description_data
            link = link[link.find('href') + 6:link.find('target') - 2]
            upload_date = item.find('pubdate').string
            upload_date = maya.parse(upload_date).datetime() + timedelta(hours=9)
            release_date = None
            news = create_news(title, source, link, upload_date, release_date)
            news_list.append(news)
            coin_id_list.append(coin['id'])
        return news_list

    def get_coin_news_from_coin_names(self, coin_names):
        news_list = []
        coin_id_list = []
        for coin_name in coin_names:
            url = self.url_parser(coin_name['coin_name'].replace(' ', ''))
            item = self.do_crawl(url, coin_id_list, coin_name)
            news_list.extend(item)
        return news_list, coin_id_list
