import requests

BINANCE_API_BASE = "https://fapi.binance.com"
TICKER_PRICE_ENDPOINT = "/fapi/v1/ticker/price"
TICKER_24HR_ENDPOINT = "/fapi/v1/ticker/24hr"

def get_sorted_coin_list():
    response = requests.get(BINANCE_API_BASE + TICKER_24HR_ENDPOINT)
    coins = response.json()
    sorted_coins = sorted(coins, key=lambda x: float(x['quoteVolume']), reverse=True)
    return [coin['symbol'] for coin in sorted_coins if 'USDT' in coin['symbol']]

def get_current_price(symbol):
    response = requests.get(BINANCE_API_BASE + TICKER_PRICE_ENDPOINT, params={'symbol': symbol})
    data = response.json()

    # If the response is a list, find the correct item
    if isinstance(data, list):
        item = next((x for x in data if x['symbol'] == symbol), None)
        return item['price'] if item else None
    else:
        # If the response is a single object, return the price
        return data.get('price')

