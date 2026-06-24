# Task 7: Mini Project - Export Discounted Prices

# Create a dictionary:

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask the user for a discount percentage.

discount = float(input("Enter Discount Percentage: "))

# Write discounted prices into discount_report.txt using:
# Product | Original Price | Discounted Price

file = open("discount_report.txt", "w")

total_discounted_price = 0

file.write("Product | Original Price | Discounted Price\n")

for product, price in prices.items():

    discounted_price = price - (price * discount / 100)

    total_discounted_price += discounted_price

    file.write(
        product + " | " +
        str(price) + " | " +
        str(discounted_price) + "\n"
    )

# Extra (Optional): Write a summary at the bottom of the file:
# Total Items: X
# Average Discounted Price: Y

average_discounted_price = (
    total_discounted_price / len(prices)
)

file.write("\n")
file.write("Total Items: " + str(len(prices)) + "\n")
file.write(
    "Average Discounted Price: " +
    str(average_discounted_price)
)

file.close()


# After writing, read the file and print it to the terminal.

file = open("discount_report.txt", "r")

print(file.read())

file.close()