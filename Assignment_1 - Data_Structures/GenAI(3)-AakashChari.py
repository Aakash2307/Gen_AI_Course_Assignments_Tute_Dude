# Task 3: Product Pricing (Dictionaries)

# 1. Create a dictionary price_dict where keys are product names and values are prices.
# Include at least 6 entries.

price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Smartwatch": 249.99,
    "Tablet": 399.99,
    "Camera": 549.99
}

print(price_dict)


# 2. Add a new product with price to price_dict.

price_dict["Printer"] = 199.99

print(price_dict)


# 2. Update the price of an existing product.

price_dict["Laptop"] = 1099.99

print(price_dict)


# 2. Remove a product by name (handle the case when the product does not exist).

product_to_remove = "Camera"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"{product_to_remove} removed successfully.")
else:
    print(f"{product_to_remove} does not exist.")

print(price_dict)


# 3. Print the average price of all products
# (use only dictionary operations and basic arithmetic).

average_price = sum(price_dict.values()) / len(price_dict)

print("Average Price:", average_price)


# Extra (Optional): Print the product with both the maximum and minimum prices.

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most Expensive Product:", max_product, "-", price_dict[max_product])
print("Least Expensive Product:", min_product, "-", price_dict[min_product])