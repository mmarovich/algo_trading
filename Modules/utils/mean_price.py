

def calc_mean_price(asks, amount):
    total_amount = 0
    price_sum = 0
    counter = 0
    mean_price = 0
    for ask in asks:
        if total_amount < amount:
            total_amount += ask[1]
            price_sum += ask[0]
            counter += 1
        else:
            mean_price = price_sum / counter
            break
        
    return mean_price