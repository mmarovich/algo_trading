from asks import all_current_asks
from bids import all_current_bids

asks = all_current_asks(1)
bids = all_current_bids(1)

def get_opportunity(amount):
    print(asks)
    highest_price = 0
    highest_ask = {}
    for ask in asks:
        if float(ask['price']) > highest_price:
            highest_price = float(ask['price'])
            highest_ask = ask

    
    print(highest_ask)
    
    lowest_price = 100000000
    lowest_bid = {}
    for bid in bids:
        if float(bid['price']) < lowest_price:
            lowest_price = float(bid['price'])
            lowest_bid = bid
    
    print(lowest_bid)
    
    profit = ((float(lowest_bid['price']) - float(highest_ask['price'])) * amount) - (0.01 * amount)
    
    if profit > 0:
        print(f"You have an opportunity to make ${profit}")
    else:
        print(f"If you made this trade you would lose ${profit}")
        
        
        
get_opportunity(1)