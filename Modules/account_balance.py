from apis_init import all_exchanges
import json


binance, phemex, mexc = all_exchanges()


def binanace_assets():
    
    binance_assets = binance.fetch_balance()['info']['balances']
    balances = []
    for asset in binance_assets:
        if float(asset['free']) > 0:
            balances.append(asset)
    
    return balances


def phemex_assets():
    
    phemex_assets = phemex.fetch_balance()
    data = phemex_assets['info']['data']
        
    balances = []
    for token in data:
        balance = {}
        balance = phemex_assets[token['currency']]
        balance['asset'] = token['currency']
        balances.append(balance)
    
    return balances

def mexc_assets():
    
    mexc_assets = mexc.fetch_balance()['info']['data']
    balances=[]
    for symbol, value in mexc_assets.items():
        balance = value
        balance['asset'] = symbol
        balances.append(balance)
        
    return balances

    
def all_balances():
    all_balances = {}
    all_balances["Binance US"] = binanace_assets()
    all_balances["Phemex"] = phemex_assets()
    all_balances["MEXC"] = mexc_assets()
    
    return all_balances
    
result = all_balances()
print(json.dumps(result, indent=2))