# Task 5: Mini Program - Safe Shopping Cart

# 1. Has a cart list.

cart = []

# 2. Runs a loop asking user to enter prices.
# 3. Stops when user enters 'q'.

while True:

    user_input = input("Enter Price (q to quit): ")

    if user_input.lower() == "q":
        break

    try:

        # 4. Inside the loop:
        # Convert input to a float.

        price = float(user_input)

        # Raise custom exception if price is negative.

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    # Handle ValueError if user enters invalid input.

    except ValueError as e:
        print("Error:", e)

# 5. At the end, print:
# Total items
# Total bill

print("Total Items:", len(cart))
print("Total Bill:", sum(cart))