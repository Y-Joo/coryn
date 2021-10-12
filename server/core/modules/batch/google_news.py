import requests
from request_parser import parse_request

url = parse_request('news/')
requests.put(url)