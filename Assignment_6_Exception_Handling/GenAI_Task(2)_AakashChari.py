# Task 2: Bill Calculator with Error Handling

# Given a list of product prices:
# prices = [120, 350, 'abc', 500, -200, 800]

prices = [120, 350, "abc", 500, -200, 800]

total = 0

# 1. Iterate through the list.

for price in prices:

    try:

        # 2. Add only valid (positive numerical) prices to the total.

        if not isinstance(price, (int, float)):
            raise TypeError("Not a valid number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price

    # 3. Handle TypeError

    except TypeError as e:
        print("Type Error:", e)

    # Handle custom exception using raise ValueError

    except ValueError as e:
        print("Value Error:", e)

# 4. Print the running total.

print("Total Bill:", total)