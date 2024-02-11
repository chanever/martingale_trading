def calculate_martingale_strategy(entry_price, drop_percent):
    return entry_price * (1 - drop_percent / 100)

def calculate_average_price(total_investment, total_coins):
    return total_investment / total_coins if total_coins else 0

def calculate_martingale(entry_price, amount, is_short=False):
    rates = [1, 2, 4, 8, 16, 32, 64]
    actions = ["sell" if is_short else "buy"]
    
    martingale_info = []
    for rate in rates:
        new_price = entry_price * (1 + (rate / 100) if is_short else 1 - (rate / 100))
        martingale_info.append(f"At {rate}% {'rise' if is_short else 'fall'}, {actions[0]} at price ${new_price:.4f}")
    
    return "\n".join(martingale_info)



