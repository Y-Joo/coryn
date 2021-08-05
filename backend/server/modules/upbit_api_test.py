import pyupbit, requests, collections
# start = time.time()
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
            coins.append(coin)
    return coins


def get_current_price(coins):
    tickers=[]
    for item in coins:
        tickers.append(item['ticker'])
    prices = pyupbit.get_current_price(tickers[:100])
    prices_2 = pyupbit.get_current_price(tickers[100:])
    prices.update(prices_2)
    price_list = []
    for coin in coins:
        price_dict = {'coin': coin['id'], 'price': prices[coin['ticker']]}
        price_list.append(price_dict)
    return price_list



# for tic in tickers:
#     print(pyupbit.get_ohlcv(tic, interval="minute1",period=0.15, count=201))
# print("time :", time.time() - start)
