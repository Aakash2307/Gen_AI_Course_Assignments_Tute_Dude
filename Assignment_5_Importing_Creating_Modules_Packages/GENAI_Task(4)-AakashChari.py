# Task 1:
# Import math_utils in two different ways

import math_utils
from math_utils import square

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(5))


# Task 2:
# Import string_utils and test all functions

import string_utils

text = "hello python world"

print("\nCapitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# Task 4:
# Importing the package in main.py

import shop_package.discount as disc

from shop_package.billing import calculate_total

print("\nDiscounted Price:")
print(disc.apply_discount(1000, 10))

print("\nFlat Discount:")
print(disc.flat_discount(1000))

print("\nTotal Bill:")
print(calculate_total([100, 200, 300]))

# Calling directly from package (__init__.py)

import shop_package

print("\nTax Applied:")
print(shop_package.apply_tax(1000))