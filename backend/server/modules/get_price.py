import pyupbit


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
