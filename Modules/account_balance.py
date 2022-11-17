from Modules.apis_init import all_exchanges
import json


binance, phemex, mexc, kraken, kucoin = all_exchanges()


def binanace_assets():
    
    binance_assets = binance.fetch_balance()['info']['balances']

    balances = []
    for asset in binance_assets:
        if float(asset['free']) > 0:
            balance = {'asset': asset['asset'], 'total': asset['free']}
            balances.append(balance)
    
    return balances


def phemex_assets():
    
    phemex_assets = phemex.fetch_balance()['free']
        
    balances = []
    for symbol, value in phemex_assets.items():
        balance = {'asset': symbol, 'total': value}
        balances.append(balance)
    
    return balances

def mexc_assets():
    
    mexc_assets = mexc.fetch_balance()['info']['data']
    balances=[]
    for symbol, value in mexc_assets.items():
        balance = {'asset': symbol, 'total': value['available']}
        balances.append(balance)
        
    return balances

def kraken_assets():
    kraken_assets = kraken.fetch_balance()['total']
    
    balances = []
    for symbol, value in kraken_assets.items():
        balances.append({'asset': symbol, 'total': value})
        
    return balances

def kucoin_assets():
    kucoin_assets = kucoin.fetch_balance()['info']['data']
    
    balances=[]
    for asset in kucoin_assets:
        if float(asset['balance']) > 0:
            balance = {'asset': asset['currency'], 'total': asset['balance']}
            balances.append(balance)
        
    return balances


kucoin_assets()
    
def all_balances():
    all_balances = {}
    all_balances["Binance US"] = binanace_assets()
    all_balances["Phemex"] = phemex_assets()
    all_balances["MEXC"] = mexc_assets()
    all_balances["Kraken"] = kraken_assets()
    all_balances["KuCoin"] = kucoin_assets()
    
    return all_balances
    
result = all_balances()
print(json.dumps(result, indent=2))