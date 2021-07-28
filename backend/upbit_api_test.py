import requests

url = "https://api.upbit.com/v1/market/all"
querystring = {"isDetails": "false"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
tickers = []
for coin in data:
    if coin['market'].split('-')[0] == "KRW":
        tickers.append([coin['market'], coin['korean_name']])
print(tickers)
#url = "https://api.upbit.com/v1/ticker"
# for tic in tickers:
#     print(tic)
#     markets = {'markets': tic}
#     response = requests.request("GET", url, headers=headers, params=markets)
#     print(response.text)
