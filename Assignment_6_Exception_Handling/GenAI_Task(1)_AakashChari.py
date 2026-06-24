# Task 1: Safe Division Utility

# 1. Take two inputs from the user:
# numerator and denominator.

try:

    numerator = float(input("Enter Numerator: "))
    denominator = float(input("Enter Denominator: "))

    # 2. Perform division.

    result = numerator / denominator

except ValueError:
    # Handle ValueError (if input is not a number)

    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    # Handle ZeroDivisionError (if denominator = 0)

    print("Error: Cannot divide by zero.")

else:
    # 3. If no error occurs, print the result inside the else block.

    print("Result:", result)

finally:
    # 4. In the finally block, print:

    print("Operation Complete")