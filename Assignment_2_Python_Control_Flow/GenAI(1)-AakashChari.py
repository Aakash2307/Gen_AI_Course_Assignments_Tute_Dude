# Task 1: Discount Rules (if / elif / else)

# 1. Write a program that reads an integer order_amount from the user using input().

order_amount = int(input("Enter order amount: "))

# 2. Apply the following discount rules and print the final amount:
# order_amount >= 2000 → 15% discount
# 1500 <= order_amount < 2000 → 10% discount
# 1000 <= order_amount < 1500 → 7% discount
# otherwise → 0% discount

if order_amount >= 2000:
    discount = 15
elif order_amount >= 1500:
    discount = 10
elif order_amount >= 1000:
    discount = 7
else:
    discount = 0

discount_amount = (order_amount * discount) / 100
final_amount = order_amount - discount_amount

print("Order Amount:", order_amount)
print("Discount:", discount, "%")
print("Final Amount:", final_amount)