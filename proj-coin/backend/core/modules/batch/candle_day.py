import requests
from request_parser import parse_request

url = parse_request('price/candle/day/')
requests.put(url)
