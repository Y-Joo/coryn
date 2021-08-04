import requests

url = "https://api.upbit.com/v1/market/all"
querystring = {"isDetails": "false"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
coins = []
for coin in data:
    if coin['market'].split('-')[0] == "KRW":
        coins.append(coin)
print(coins)