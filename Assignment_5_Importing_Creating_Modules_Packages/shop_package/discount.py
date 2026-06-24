# discount.py

# 1. apply_discount(price, percent)
# returns discounted price

def apply_discount(price, percent):
    return price - (price * percent / 100)


# 2. flat_discount(price)
# always subtracts 50 from price

def flat_discount(price):
    return price - 50