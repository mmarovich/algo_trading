from Modules.apis_init import all_exchanges
import datetime

binance, phemex, mexc, kraken = all_exchanges()


# binance_markets = binance.load_markets()

# symbols = ['USDC', 'USDT']
# for item in binance_markets:
#     if any(x in item for x in symbols):
#         print(item, end=" || ")
    
days_to_now = 500
symbol = 'BTC/USDT'
interval = '1d'

def get_history(account):
    dt_obj = datetime.datetime.now() - datetime.timedelta(days_to_now)

    # api takes time in milliseconds
    dt_obj = millisec = dt_obj.timestamp() * 1000
    history = account.fetch_ohlcv(symbol, timeframe=interval, since=millisec, params={'price': 'index'})
    
    return history

# result = get_history(binance)
# print(result)