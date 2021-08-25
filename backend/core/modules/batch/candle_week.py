import requests
from request_parser import parse_request

url = parse_request('price/candle/week/')
requests.put(url)
