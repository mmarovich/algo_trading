import ccxt
from Modules.exchanges import exchange_list
from dotenv import load_dotenv
import os

load_dotenv()

exchanges = exchange_list


def getExchanges():
    for exchange in exchanges:
        print(exchange['name'], end=" || ")
    
    

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
    
    kraken = ccxt.kraken({
        'enableRateLimit': True,
        'apiKey': os.getenv("KRAKEN_API_KEY"),
        'secret': os.getenv("KRAKEN_API_SECRET")
    })
    
    kucoin = ccxt.kucoin({
        'enableRateLimit': True,
        'apiKey': os.getenv("KUCOIN_API_KEY"),
        'secret': os.getenv("KUCOIN_API_SECRET"),
        'password': os.getenv("KUCOIN_API_PASSPHRASE")
    })
    
    
    return binance, phemex, mexc, kraken, kucoin

