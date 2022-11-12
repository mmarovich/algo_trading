import ccxt
import exchanges
from dotenv import load_dotenv
import os

load_dotenv()

exchanges = exchanges.exchange_list


# def getExchanges():
#     for exchange in exchanges:
#         print(exchange['name'], end=" || ")
        
# getExchanges()
    
    

def all_exchanges():
    binance = ccxt.binanceus({
        'enableRateLimit': True,
        'apiKey': os.getenv("BINANCE_API_KEY"),
        'secret': os.getenv("BINANCE_API_SECRET")
    })
    
    phemex = ccxt.phemex({
        'enableRateLimit': True,
        'apiKey': os.getenv("PHEMEX_API_ID"),
        'secret': os.getenv("PHEMEX_API_SECRET")
    })
    
    mexc = ccxt.mexc({
        'enableRateLimit': True,
        'apiKey': os.getenv("MEXC_API_KEY"),
        'secret': os.getenv("MEXC_API_SECRET")
    })
    
    
    return binance, phemex, mexc

