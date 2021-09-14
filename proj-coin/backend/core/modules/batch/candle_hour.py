import requests
from request_parser import parse_request

url = parse_request('price/candle/hour/')
requests.put(url)
