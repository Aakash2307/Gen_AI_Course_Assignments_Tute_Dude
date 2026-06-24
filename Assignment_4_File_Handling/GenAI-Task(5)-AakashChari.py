# Task 5: Create Product Info File (User Input)

# 1. Ask the user for 3 product names and their prices.

file = open("products.txt", "w")

for i in range(3):

    product_name = input("Enter Product Name: ")
    price = input("Enter Price: ")

    # 2. Write them to a new file products.txt in this format:
    # ProductName | Price

    file.write(product_name + " | " + price + "\n")

file.close()


# 3. Read the file and print each line with proper formatting.

file = open("products.txt", "r")

for line in file:
    print(line.strip())

file.close()