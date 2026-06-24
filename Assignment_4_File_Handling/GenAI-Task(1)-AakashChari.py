# Task 1: Write Sales Records to a File

# 1. Create a list of sales amounts:
# sales = [1200, 450, 980, 1500, 3000]

sales = [1200, 450, 980, 1500, 3000]

# 2. Open a file named sales_data.txt in write mode.

file = open("sales_data.txt", "w")

# 3. Write each sale on a new line in the file.

for sale in sales:
    file.write(str(sale) + "\n")

# 4. Close the file, then reopen it and print its contents.

file.close()

file = open("sales_data.txt", "r")

print(file.read())

file.close()