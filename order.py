import datetime
import time
import requests
from .funcs import funcs
from .binance_handler import _check_symbol

MAINLINK = " https://fapi.binance.com"

def now_timestamp():
    return int(round(time.time() * 1000))-2500
def binance_timestamp():  
    rs = requests.get("https://fapi.binance.com/fapi/v1/time")
    return rs.json()['serverTime']

def _new_order(**kwargs):
    lnk = MAINLINK + "/fapi/v1/order"
    rq = funcs.post_v3(lnk,**kwargs)
    return rq

# def _send_order()

def _buy_order(**kwargs):
    _check_symbol(kwargs["symbol"])
    data = {"side":"BUY","recvWindow": 5000,"timestamp": now_timestamp()}
    kwargs.update(data)
    lnk = MAINLINK + "/fapi/v1/order"
    rq = funcs.post_v3(lnk,**kwargs)
    print(rq.json())
    return rq

def _sell_order(**kwargs):
    _check_symbol(kwargs["symbol"])

    data = {"side":"SELL","recvWindow": 5000,"timestamp": now_timestamp()}
    kwargs.update(data)
    lnk = MAINLINK + "/fapi/v1/order"
    rq = funcs.post_v3(lnk,**kwargs)
    print(rq.json())
    return rq


def market_sell_order(symbol:str,quantity:int|float )-> requests.Response:
    return _sell_order(symbol=symbol,quantity=quantity,type="MARKET")


def market_buy_order(symbol:str,quantity:int|float )-> requests.Response:
    return _buy_order(symbol=symbol,quantity=quantity,type="MARKET")



# print(market_buy_order("XRPUSDT",10).content)
"""{
    "symbol":	STRING	YES
"side":	ENUM	YES
"positionSide":	ENUM	NO
"type":	ENUM	YES
"timeInForce":	ENUM	NO
"quantity":	DECIMAL	NO
"reduceOnly":	STRING	NO
"price":	DECIMAL	NO
"newClientOrderId":	STRING	NO
"stopPrice":	DECIMAL	NO
"closePosition":	STRING	NO
"activationPrice":	DECIMAL	NO
"callbackRate":	DECIMAL	NO
"workingType":	ENUM	NO
"priceProtect":	STRING	NO
"newOrderRespType":	ENUM	NO
"priceMatch":	ENUM	NO
"selfTradePreventionMode":	ENUM	NO
"goodTillDate":	LONG	NO
"recvWindow":	LONG	NO
"timestamp":	LONG	YES
}"""