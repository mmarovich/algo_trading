from Modules.apis_init import all_exchanges
from Modules.utils.mean_price import calc_mean_price

binance, phemex, mexc, kraken, kucoin = all_exchanges()

days_to_now = 1
symbol = 'BTC/USDT'
interval = '1d'

def get_asks(account, amount):
    
    ob = account.fetch_order_book(symbol)
    asks = ob['asks']
    
    mean_price = calc_mean_price(asks, amount)
    
    return mean_price


def all_current_asks(amount):
    binance_ask = get_asks(binance, amount)
    phemex_ask = get_asks(phemex, amount)
    mexc_ask = get_asks(mexc, amount)
    kraken_ask = get_asks(kraken, amount)
    kucoin_ask = get_asks(kucoin, amount)
    
    all_asks = [
        {'id': 'binanceus', 'symbol': symbol, 'price': binance_ask},
        {'id': 'phemex', 'symbol': symbol, 'price': phemex_ask},
        {'id': 'mexc', 'symbol': symbol, 'price': mexc_ask},
        {'id': 'kraken', 'symbol': symbol, 'price': kraken_ask},
        {'id': 'kucoin', 'symbol': symbol, 'price': kucoin_ask}
    ]
    
    return all_asks

# result = all_current_asks(1)
# print(result)