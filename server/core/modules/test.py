import pyupbit, time
start = time.time()
tickers = pyupbit.get_tickers()
for tic in tickers:
    candles = (pyupbit.get_ohlcv(tic, interval="minute1", period=0.12, count=201).values.tolist())
print(time.time() - start)
