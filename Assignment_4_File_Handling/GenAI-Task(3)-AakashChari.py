# Task 3: Append New Sales

# 1. Append these new sales to the same file:
# 5000, 2500, 1700

file = open("sales_data.txt", "a")

file.write("5000\n")
file.write("2500\n")
file.write("1700\n")

file.close()


# 2. After appending, reopen and print the entire updated file.

file = open("sales_data.txt", "r")

print(file.read())

file.close()


# Extra (Optional): Print the total number of lines after appending.

file = open("sales_data.txt", "r")

line_count = len(file.readlines())

print("Total Lines:", line_count)

file.close()