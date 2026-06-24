# Task 4: Generate Summary Report from File

# 1. Read all sales values from sales_data.txt.

file = open("sales_data.txt", "r")

lines = file.readlines()

file.close()

# 2. Convert them into integers.

sales = []

for line in lines:
    sales.append(int(line.strip()))

# 3. Calculate and print:
# Total Sales
# Highest Sale
# Lowest Sale
# Average Sale

total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)