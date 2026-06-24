# Task 4: Combined Operations

# 1. Using the products list and price_dict, create a list of tuples named catalog
# where each tuple is (product_name, price, category).


price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Smartwatch": 249.99,
    "Tablet": 399.99,
    "Camera": 549.99
}


catalog = [
    ("Laptop", price_dict["Laptop"], "Electronics"),
    ("Smartphone", price_dict["Smartphone"], "Mobile"),
    ("Headphones", price_dict["Headphones"], "Audio"),
    ("Smartwatch", price_dict["Smartwatch"], "Wearables"),
    ("Tablet", price_dict["Tablet"], "Electronics"),
    ("Printer", price_dict["Printer"], "Accessories")
]

print("Catalog:")
for item in catalog:
    print(item)


# 2. From catalog, create a new dictionary category_to_products
# that maps each category to a list of product names in that category.

category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product_name)

print("\nCategory to Products:")
print(category_to_products)


# 3. Print all products that belong to the category
# that has the maximum number of products.

max_category = max(
    category_to_products,
    key=lambda category: len(category_to_products[category])
)

print("\nCategory with Maximum Products:", max_category)
print("Products:")

for product in category_to_products[max_category]:
    print(product)