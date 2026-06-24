# Task 4: Using map() - Apply GST to List of Prices

# Given:
# prices = [100, 250, 400, 1200, 50]

prices = [100, 250, 400, 1200, 50]

# Use map() with your gst lambda to generate a new list prices_with_gst.

gst = lambda price: price + (0.18 * price)

prices_with_gst = list(map(gst, prices))

# Print both lists:
# Original prices
# Prices after GST

print("Original Prices:", prices)
print("Prices After GST:", prices_with_gst)