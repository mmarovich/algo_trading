from Modules.apis_init import all_exchanges

binance, phemex, mexc, kraken, kucoin = all_exchanges()

symbols = ['USDC', 'USDT']

def binance_pairs():
    binance_markets = binance.load_markets()

    for item in binance_markets:
        if any(x in item for x in symbols):
            print(item, end=" || ")
            
def phemex_pairs():
    phemex_markets = phemex.load_markets()

    for item in phemex_markets:
        if any(x in item for x in symbols):
            print(item, end=" || ")
            
def mexc_pairs():
    mexc_markets = mexc.load_markets()

    for item in mexc_markets:
        if any(x in item for x in symbols):
            print(item, end=" || ")
            
def kraken_pairs():
    kraken_markets = kraken.load_markets()

    for item in kraken_markets:
        if any(x in item for x in symbols):
            print(item, end=" || ")
            
def kucoin_pairs():
    kucoin_markets = kucoin.load_markets()

    for item in kucoin_markets:
        if any(x in item for x in symbols):
            print(item, end=" || ")
            
# kucoin_pairs()