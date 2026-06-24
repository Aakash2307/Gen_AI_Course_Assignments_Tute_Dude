# Task 5: Using filter() - Filter Expensive Products

# Given the list:
# prices = [100, 250, 400, 1200, 50, 2000, 850]

prices = [100, 250, 400, 1200, 50, 2000, 850]

# Use filter() to:
# 1. Create a list of prices greater than 500.

greater_than_500 = list(filter(lambda x: x > 500, prices))

# 2. Create another list of prices less than or equal to 500.

less_than_equal_500 = list(filter(lambda x: x <= 500, prices))

# Print both lists.

print("Prices > 500:", greater_than_500)
print("Prices <= 500:", less_than_equal_500)