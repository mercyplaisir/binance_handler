import requests
import json

def exchange_information():
    main_lnk = "https://fapi.binance.com/"
    lnk = main_lnk + "/fapi/v1/exchangeInfo"

    req = requests.get(lnk)

    with open("binance_exchange_info.json","wb") as f:
        f.write(req.content)

def open_json(filepath):
    with open(filepath,'r') as f:
        d = json.load(f)
    return d

# exchange_information()

def pair_price(pair:str) -> float:
    main_lnk = "https://fapi.binance.com/"
    lnk = main_lnk + "/fapi/v1/ticker/price"

    rq = requests.get(lnk,params={"symbol":pair})

    return float(rq.json()["price"])

def future_symbols():
    data = open_json("data/binance_exchange_info.json")
    symbols = [symbol_data['symbol'] for symbol_data in data['symbols']]
    return symbols
    ...


def minimum_margin(symbol:str) -> None:
    data = open_json("data/restructured_data.json")
    
    new_data = float(data[symbol]['filters'][5]['notional'])+2
    


    return new_data

# print(minimum_margin("BTCUSDT"))
print(future_symbols())
