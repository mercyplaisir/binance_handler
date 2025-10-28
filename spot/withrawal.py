from ..funcs import funcs
import requests 
import time
from ..errors.errors import WithdrawalError

base_url = 'https://api.binance.com'
url_endpoint ="/sapi/v1/capital/withdraw/apply"


def withdraw(address, amount, coin:str="USDC", network:str=None, address_tag:str=None, name:str=None, wallet_type:int=0 ):
    """
    Withdraws a specified amount of currency to a given address.
    
    :param address: The address to which the funds will be withdrawn.
    :param amount: The amount of currency to withdraw.
    :param currency: The type of currency to withdraw (e.g., 'BTC', 'ETH').
    :return: A confirmation message or an error message.
    """
    
    kwargs = {
        "coin": coin,
        "address": address,
        "amount": amount,
        "network": network,
        "addressTag": address_tag,
        "name": name,
        "walletType": wallet_type,
        "recvWindow": 5000,
        "timestamp": int(round(time.time() * 1000)) - 2500
    }
    
    response = funcs.post_v3(url=base_url + url_endpoint, **kwargs)
    
    if response.status_code == 200:
        return response.json()
    
    else:
        raise WithdrawalError
    