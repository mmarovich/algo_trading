from Modules.asks import all_current_asks
from Modules.bids import all_current_bids
from Modules.send_email import send_email
import time

def get_opportunity(amount):
    
    asks = all_current_asks(1)
    bids = all_current_bids(1)
    
    print(f"all of the asking prices: {asks}")
    print("")
    print(f"All of the bids prices: {bids}")
    print("")
    print("")
    
    lowest_price = 10000000000
    lowest_ask = {}
    for ask in asks:
        if float(ask['price']) < lowest_price:
            lowest_price = float(ask['price'])
            lowest_ask = ask

    
    print(f"The lowest asking price: {lowest_ask}")

    highest_price = 0
    highest_bid = {}
    for bid in bids:
        if float(bid['price']) > highest_price:
            highest_price = float(bid['price'])
            highest_bid = bid
    
    print(f"The highest bid is: {highest_bid}")
    print("")
    print("")
    
    fee1 = (0.001 * amount) * lowest_price
    fee2 = (0.001 * amount) * highest_price
    
    profit = ((float(highest_bid['price']) - float(lowest_ask['price'])) * amount)
    profit_with_fees = ((float(highest_bid['price']) - float(lowest_ask['price'])) * amount) - (fee1 + fee2)
    
    if profit_with_fees > 0:
        print(f"You have an opportunity to make ${profit}")
        send_email(lowest_ask['id'], lowest_ask['price'], highest_bid['id'], highest_bid['price'], profit_with_fees)
    else:
        print(f"If you made this trade you would lose ${round(abs(profit_with_fees), 2)}, ${round(abs(profit_with_fees) - profit, 2)} of that is because of fees")
        send_email(lowest_ask['id'], lowest_ask['price'], highest_bid['id'], highest_bid['price'], profit_with_fees)
        
def run():
    while True:
        get_opportunity(1)
        time.sleep(60 * 1)
        print("||||||||||||||||||||||||||||")
            

            
run()