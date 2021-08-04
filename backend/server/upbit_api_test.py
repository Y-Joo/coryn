import pyupbit, requests
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
            coins.append(coin)
    return coins

# print(pyupbit.get_current_price(tickers[:100]))
# print(pyupbit.get_current_price(tickers[100:]))
# for tic in tickers:
#     print(pyupbit.get_ohlcv(tic, interval="minute1",period=0.15, count=201))
# print("time :", time.time() - start)
