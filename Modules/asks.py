from apis_init import all_exchanges
from utils.mean_price import calc_mean_price

binance, phemex, mexc = all_exchanges()

days_to_now = 1
symbol = 'BTC/USDT'
interval = '1d'


def binance_asks(amount):
    
    ob = binance.fetch_order_book(symbol)
    asks = ob['asks']
    
    mean_price = calc_mean_price(asks, amount)
            
    return mean_price

def phemex_asks(amount):
    
    ob = phemex.fetch_order_book(symbol)
    asks = ob['asks']
    
    mean_price = calc_mean_price(asks, amount)
            
    return mean_price


def mexc_asks(amount):
    
    ob = mexc.fetch_order_book(symbol)
    asks = ob['asks']
    
    mean_price = calc_mean_price(asks, amount)
    
    return mean_price

def all_current_asks(amount):
    binance_ask = binance_asks(amount)
    phemex_ask = phemex_asks(amount)
    mexc_ask = mexc_asks(amount)
    
    all_asks = [
        {'id': 'binanceus', 'symbol': symbol, 'price': binance_ask},
        {'id': 'phemex', 'symbol': symbol, 'price': phemex_ask},
        {'id': 'mexc', 'symbol': symbol, 'price': mexc_ask}
    ]
    
    return all_asks