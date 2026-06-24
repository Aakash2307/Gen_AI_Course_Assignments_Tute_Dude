# Task 2: Categories (Sets)

# 1. From your products list, create a set of categories called categories_set.

categories_set = {
    "Electronics",
    "Mobile",
    "Audio",
    "Wearables",
    "Photography"
}

print(categories_set)


# 2. Demonstrate adding a new category to the set and show that duplicates are ignored.

categories_set.add("Gaming")
categories_set.add("Electronics")  # Duplicate category

print(categories_set)


# 3. Show how to check whether a category exists in the set (print a boolean result).

print("Gaming" in categories_set)
print("Furniture" in categories_set)


# Extra (Optional): Show how to get the total number of unique categories using a set.

print("Total unique categories:", len(categories_set))