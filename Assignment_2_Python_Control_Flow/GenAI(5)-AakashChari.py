# Task 5: Loop Control with Conditions (break & continue)

# 1. Given a list of daily sales:
# daily = [200, 150, 0, 400, 50, -1, 300]

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    # If a day's value is -1, treat it as corrupted data and break the loop.

    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

    # If a day's value is 0, treat it as a day with no sales and continue.

    if sale == 0:
        print("No sales today. Skipping.")
        continue

    # For valid positive sales, add to total_sales and print running total.

    total_sales += sale

    print("Running Total:", total_sales)

# 2. Print the final total after the loop completes.

print("Final Total Sales:", total_sales)