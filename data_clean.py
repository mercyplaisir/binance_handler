import json
with open("binance_exchange_info.json","r")as f:
    data = json.load(f)

def save_data(data,filename) ->None	:
    with open(filename,'w') as f:
        d = json.dumps(data)
        f.write(d)

def restucture(data):
    new_data = {}
    for symbol_data in data['symbols']:
        symbol = symbol_data['symbol']
        new_data[symbol] = symbol_data
    save_data(new_data,"restructured_data.json")
    


restucture(data)