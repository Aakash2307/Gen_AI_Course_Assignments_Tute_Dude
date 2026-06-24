# Task 3: Lambda Function - GST Calculator

# Create a lambda function gst that returns price after adding 18% GST.

gst = lambda price: price + (0.18 * price)

# Example:
# print(gst(100)) should return 118

print(gst(100))


# Extra (Optional): Create another lambda to compute final price after GST + discount.

final_price = lambda price, discount: (price + (0.18 * price)) - ((price + (0.18 * price)) * discount / 100)

print(final_price(1000, 10))