import requests


def crawl_coin_name():
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails": "false"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    coins = []
    for coin in data:
        if coin['market'].split('-')[0] == "KRW":
            coin['ticker'] = coin.pop('market')
            coin['kr_name'] = coin.pop('korean_name')
            coin['coin_name'] = coin.pop('english_name')
            coin['coin_img'] = 'https://static.upbit.com/logos/' + coin['ticker'].split('-')[1] + '.png'
            coins.append(coin)
    return coins

