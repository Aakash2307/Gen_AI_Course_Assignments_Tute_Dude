# Task 2: Read File in Different Ways

# Using the same sales_data.txt:

# 1. Read the entire file using .read() and print it.

file = open("sales_data.txt", "r")

print("Using read():")
print(file.read())

file.close()


# 2. Read the first line using .readline().

file = open("sales_data.txt", "r")

print("Using readline():")
print(file.readline())

file.close()


# 3. Read all lines using .readlines()
# and convert them into a list of integers.

file = open("sales_data.txt", "r")

lines = file.readlines()

sales = []

for line in lines:
    sales.append(int(line.strip()))

print("Using readlines():")
print(sales)

file.close()