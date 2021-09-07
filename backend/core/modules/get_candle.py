import pyupbit


def get_minute_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="minute1", period=0.15, count=201).values.tolist())
        high = ""
        low = ""
        open = ""
        close = ""
        for candle in candles:
            if high == "":
                open += str(candle[0])
                high += str(candle[1])
                low += str(candle[2])
                close += str(candle[3])
            else:
                open += ',' + str(candle[0])
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
                close += ',' + str(candle[3])
        candle_dict = {'minute_high': high, 'minute_low': low, 'minute_open': open, 'minute_close': close, 'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_hour_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="minute60", period=0.15, count=201).values.tolist())
        high = ""
        low = ""
        open = ""
        close = ""
        for candle in candles:
            if high == "":
                open += str(candle[0])
                high += str(candle[1])
                low += str(candle[2])
                close += str(candle[3])
            else:
                open += ',' + str(candle[0])
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
                close += ',' + str(candle[3])
        candle_dict = {'hour_high': high, 'hour_low': low, 'hour_open': open, 'hour_close': close,
                       'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_day_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="day", period=0.15, count=201).values.tolist())
        high = ""
        low = ""
        open = ""
        close = ""
        for candle in candles:
            if high == "":
                open += str(candle[0])
                high += str(candle[1])
                low += str(candle[2])
                close += str(candle[3])
            else:
                open += ',' + str(candle[0])
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
                close += ',' + str(candle[3])
        candle_dict = {'day_high': high, 'day_low': low, 'day_open': open, 'day_close': close,
                       'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list


def get_week_candle(coins):
    candle_list = []
    for coin in coins:
        candles = (pyupbit.get_ohlcv(coin['ticker'], interval="week", period=0.15, count=201).values.tolist())
        high = ""
        low = ""
        open = ""
        close = ""
        for candle in candles:
            if high == "":
                open += str(candle[0])
                high += str(candle[1])
                low += str(candle[2])
                close += str(candle[3])
            else:
                open += ',' + str(candle[0])
                high += ',' + str(candle[1])
                low += ',' + str(candle[2])
                close += ',' + str(candle[3])
        candle_dict = {'week_high': high, 'week_low': low, 'week_open': open, 'week_close': close,
                       'coin': coin['id']}
        candle_list.append(candle_dict)
    return candle_list