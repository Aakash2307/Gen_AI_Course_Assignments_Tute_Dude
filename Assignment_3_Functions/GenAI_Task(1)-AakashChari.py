# Task 1: Basic Function - Price After Discount

# 1. Write a function apply_discount(price, discount_percent) that:
# Returns the price after discount.

# 2. If discount_percent is missing, apply a default discount of 5%.

def apply_discount(price, discount_percent=5):

    # Extra (Optional): Ensure discount never exceeds 60%.

    if discount_percent > 60:
        discount_percent = 60

    final_price = price - (price * discount_percent / 100)

    return final_price


# 3. Test the function with:
# apply_discount(1000, 10)

print(apply_discount(1000, 10))

# 4. apply_discount(500) uses default discount.

print(apply_discount(500))