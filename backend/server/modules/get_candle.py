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
        candle_dict = {'minute_high': high, 'minute_low': low, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_hour_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="minute60", period=0.15, count=201).values.tolist())
        high = ""

        low = ""
        for candle in candles:
            if high == "":
                high += str(candle[1])
                low += str(candle[2])
            else:
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
        candle_dict = {'hour_high': high, 'hour_low': low, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_day_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="day", period=0.15, count=201).values.tolist())
        high = ""

        low = ""
        for candle in candles:
            if high == "":
                high += str(candle[1])
                low += str(candle[2])
            else:
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
        candle_dict = {'day_high': high, 'day_low': low, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_week_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="week", period=0.15, count=201).values.tolist())
        high = ""
        low = ""
        for candle in candles:
            if high == "":
                high += str(candle[1])
                low += str(candle[2])
            else:
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
        candle_dict = {'week_high': high, 'week_low': low, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list