from Modules.apis_init import all_exchanges
from Modules.utils.mean_price import calc_mean_price

binance, phemex, mexc, kraken, kucoin = all_exchanges()

days_to_now = 1
symbol = 'BTC/USDT'
interval = '1d'

def get_bids(account, amount):
    
    ob = account.fetch_order_book(symbol)
    asks = ob['asks']
    
    mean_price = calc_mean_price(asks, amount)
    
    return mean_price

def all_current_bids(amount):
    binance_bid = get_bids(binance, amount)
    phemex_bid = get_bids(phemex, amount)
    mexc_bid = get_bids(mexc, amount)
    kraken_bid = get_bids(kraken, amount)
    kucoin_bid = get_bids(kucoin, amount)
    
    all_bids = [
        {'id': 'phemex', 'symbol': symbol, 'price': phemex_bid},
        {'id': 'binanceus', 'symbol': symbol, 'price': binance_bid},
        {'id': 'mexc', 'symbol': symbol, 'price': mexc_bid},
        {'id': 'kraken', 'symbol': symbol, 'price': kraken_bid},
        {'id': 'kucoin', 'symbol': symbol, 'price': kucoin_bid}
    ]
    
    return all_bids

# result = all_current_bids(1)
# print(result)