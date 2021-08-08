import pyupbit


def get_minute_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="minute1", period=0.15, count=201).values.tolist())
        high = ""

        low = ""
        for candle in candles:
            if high == "":
                high += str(candle[1])
                low += str(candle[2])
            else:
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
        candle_dict = {'high': high, 'low': low, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list
