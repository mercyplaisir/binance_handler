from ..funcs import funcs
import requests
import time
base_url = 'https://api.binance.com'
url_endpoint = '/sapi/v1/pay/transactions'

def now_timestamp():
    return int(round(time.time() * 1000))-2500

def get_payment_history(start:int|float,end:int|float)->requests.Response :
    kwargs = { "recvWindow": 5000,"timestamp": now_timestamp() }
    return funcs.get_v3(url=base_url+url_endpoint,startTime=start,endTime=end,**kwargs)