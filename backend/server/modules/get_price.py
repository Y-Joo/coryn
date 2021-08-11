import pyupbit


def get_current_price(coins):
    tickers = []
    for item in coins:
        tickers.append(item['ticker'])
    prices = pyupbit.get_current_price(tickers[:100])
    prices_2 = pyupbit.get_current_price(tickers[100:])
    prices.update(prices_2)
    price_list = []
    for coin in coins:
        day_open = float(coin['coin_price__day_open'].split(',')[-1])
        change = round(float((prices[coin['ticker']] - day_open)/day_open * 100), 2)
        print(day_open, prices[coin['ticker']], change)
        price_dict = {'coin': coin['id'], 'price': prices[coin['ticker']], 'day_change': change}
        price_list.append(price_dict)
    return price_list
