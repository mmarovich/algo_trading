from Modules.apis_init import all_exchanges

binance, phemex, mexc, kraken = all_exchanges()

days_to_now = 1
# symbol = 'BTC/USDT'
interval = '1d'

def current_price():
    
    ob = binance.fetch_order_book('BTC/USDT')
    print(ob)
    
current_price()