from bs4 import BeautifulSoup
from urllib.request import urlopen
import maya
import time
from datetime import timedelta


class CrawlerGoogle:
    @staticmethod
    def url_parser(coin: str):
        url = 'https://news.google.com/rss/search?q=' + coin + '+when:1d&hl=en-NG&gl=NG&ceid=NG:en'
        return url

    @staticmethod
    def create_news(title, source, link, upload_date, release_date):
        news = {
            'type': 0,
            'title': title,
            'source': source,
            'link': link,
            'upload_date': upload_date,
            'release_date': release_date,
        }
        return news

    def crawl(self, url: str, coin_id_list, coin):
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
            news = self.create_news(title, source, link, upload_date, release_date)
            news_list.append(news)
            coin_id_list.append(coin['id'])
        return news_list

    def crawl_coin_list(self, coin_list):
        news_list = []
        coin_id_list = []
        for coin in coin_list:
            url = self.url_parser(coin['coin_name'].replace(' ', ''))
            item = self.crawl(url, coin_id_list, coin)
            news_list.extend(item)
        return news_list, coin_id_list
