# Task 2: Recursive Function - Factorial Utility

# Create a recursive function factorial(n) that:
# 1. Returns the factorial of n.
# 2. Handles two edge cases: n == 0 and n == 1.
# 3. Prints an error message if n is negative.

def factorial(n):

    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Test with:
# factorial(5)

print(factorial(5))

# factorial(0)

print(factorial(0))

# factorial(-3)

print(factorial(-3))