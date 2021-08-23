import collections
import crawl_coinmarketcal as coinmarketcal


def preprocessingDict(dic: dict):
    coin_dict = collections.defaultdict(dict)
    for key, value in dic.items():
        if value['symbol'] in coin_dict[value['date']]:
            coin_dict[value['date']][value['symbol']].append([key, value['title'], value['name']])
        else:
            coin_dict[value['date']][value['symbol']] = [[key, value['title'], value['name']]]
    return coin_dict


def crontab():
    result = dict()

    urls = coinmarketcal.get_urls()
    for url in urls:
        coinmarketcal.do_crawl(url, result)