# billing.py

# 1. calculate_total(prices)
# returns total bill

def calculate_total(prices):
    return sum(prices)


# 2. apply_tax(amount)
# adds 5% tax

def apply_tax(amount):
    return amount + (amount * 0.05)