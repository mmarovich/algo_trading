from apis_init import all_exchanges
import datetime

binance, phemex, mexc = all_exchanges()


# binance_markets = binance.load_markets()

# symbols = ['USDC', 'USDT']
# for item in binance_markets:
#     if any(x in item for x in symbols):
#         print(item, end=" || ")
    
days_to_now = 500
symbol = 'BTC/USDT'
interval = '1d'

def binance_history():
    #binance limitation is 500 items per data set (ie: 500 days at '1d' or 250 days at '12h')
    dt_obj = datetime.datetime.now() - datetime.timedelta(days_to_now)

    # api takes time in milliseconds
    dt_obj = millisec = dt_obj.timestamp() * 1000
    binance_history = binance.fetch_ohlcv(symbol, timeframe=interval, since=millisec, params={'price': 'index'})

    return binance_history



def phemex_history():
    #binance limitation is 599 items per data set (ie: 599 days at '1d')
    dt_obj = datetime.datetime.now() - datetime.timedelta(days_to_now)

    # api takes time in milliseconds
    dt_obj = millisec = dt_obj.timestamp() * 1000
    phemex_history = phemex.fetch_ohlcv(symbol, timeframe=interval, since=millisec, params={'price': 'index'})
    
    return phemex_history

def mexc_history():
    #mexc limitation is 100 items per data set (ie: 100 days at '1d')
    dt_obj = datetime.datetime.now() - datetime.timedelta(days_to_now)

    # api takes time in milliseconds
    dt_obj = millisec = dt_obj.timestamp() * 1000
    mexc_history = mexc.fetch_ohlcv(symbol, timeframe=interval, since=millisec, params={'price': 'index'})
    
    return mexc_history