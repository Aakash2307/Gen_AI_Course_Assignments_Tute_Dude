# Task 6: Combined Utility Function

# Write a function process_prices(prices) that:
# 1. Takes a list of prices.
# 2. Uses map() + lambda to apply 10% discount to all prices.
# 3. Uses filter() to keep only discounted prices that are above 300.
# 4. Returns both lists:
#    discounted_prices
#    filtered_prices

def process_prices(prices):

    discounted_prices = list(
        map(lambda price: price * 0.90, prices)
    )

    filtered_prices = list(
        filter(lambda price: price > 300, discounted_prices)
    )

    return discounted_prices, filtered_prices


# Test with:
# process_prices([100, 500, 900, 50, 750])

discounted_prices, filtered_prices = process_prices(
    [100, 500, 900, 50, 750]
)

print("Discounted Prices:", discounted_prices)
print("Filtered Prices:", filtered_prices)