from apis_init import all_exchanges
from utils.mean_price import calc_mean_price

binance, phemex, mexc = all_exchanges()

days_to_now = 1
symbol = 'BTC/USDT'
interval = '1d'

def binance_bids(amount):
    
    ob = binance.fetch_order_book(symbol)
    bids = ob['bids']
    
    mean_price = calc_mean_price(bids, amount)
    
    return mean_price

def phemex_bids(amount):
    
    ob = phemex.fetch_order_book(symbol)
    bids = ob['bids']
    
    mean_price = calc_mean_price(bids, amount)
    
    return mean_price

def mexc_bids(amount):
    
    ob = mexc.fetch_order_book(symbol)
    bids = ob['bids']
    
    mean_price = calc_mean_price(bids, amount)
    
    return mean_price

def all_current_bids(amount):
    binance_bid = binance_bids(amount)
    phemex_bid = phemex_bids(amount)
    mexc_bid = mexc_bids(amount)
    
    all_bids = [
        {'id': 'phemex', 'symbol': symbol, 'price': phemex_bid},
        {'id': 'binanceus', 'symbol': symbol, 'price': binance_bid},
        {'id': 'mexc', 'symbol': symbol, 'price': mexc_bid}
    ]
    
    return all_bids