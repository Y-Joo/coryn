import requests

url = "https://api.upbit.com/v1/market/all"
querystring = {"isDetails": "false"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
tickers = []
for coin in data:
    tickers.append(coin['market'])
print(tickers)
#url = "https://api.upbit.com/v1/ticker"
# for tic in tickers:
#     print(tic)
#     markets = {'markets': tic}
#     response = requests.request("GET", url, headers=headers, params=markets)
#     print(response.text)
