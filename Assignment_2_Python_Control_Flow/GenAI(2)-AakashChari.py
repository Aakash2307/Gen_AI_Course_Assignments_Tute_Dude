# Task 2: Process Multiple Orders (for loop)

# 1. Given a list of order amounts:
# orders = [1200, 2500, 800, 1750, 3000]
# use a for loop to apply the discount rules from Task 1
# and print a summary table showing:
# order_amount -> discount% -> final_amount

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0

print("Order\tDiscount\tFinal Amount")

for order in orders:

    if order >= 2000:
        discount = 15
    elif order >= 1500:
        discount = 10
    elif order >= 1000:
        discount = 7
    else:
        discount = 0

    final_amount = order - ((order * discount) / 100)

    print(order, "\t", str(discount) + "%", "\t\t", final_amount)

    total_revenue += final_amount

# 2. Also compute and print the total revenue after discounts.

print("\nTotal Revenue:", total_revenue)