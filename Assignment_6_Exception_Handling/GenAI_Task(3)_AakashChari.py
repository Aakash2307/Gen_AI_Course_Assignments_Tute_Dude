# Task 3: Custom Exception - Age Validator

# 1. Write a function check_age(age) that:
# Raises a custom exception ValueError
# ("Age must be between 1 and 120")
# if age is out of range.

def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    print("Valid Age")


# 2. In your main code:
# Take age input from the user.

try:

    age = int(input("Enter Age: "))

    check_age(age)

# Use try-except to catch and print the custom error message.

except ValueError as e:
    print(e)