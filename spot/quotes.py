import requests
def get_quote(symbol: str) -> float|None:
    """
    Fetches the latest market quotes for a given symbol from Binance API.

    Args:
        symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
        """
    base_url = "https://api.binance.com"
    endpoint = "/api/v3/ticker/price"
    params = {"symbol": symbol.upper()}

    response = requests.get(f"{base_url}{endpoint}", params=params)
    response.raise_for_status()  # Raise an error for bad responses

    return response.json().get("price", None)

if __name__ == "__main__":
    symbol = "BTCUSDT"
    quote = get_quote(symbol)
    print(f"Latest quote for {symbol}: {quote}")