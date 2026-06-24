# Task 7: Mini Problem - Menu Using Functions

# Create the following three small functions:
# 1. add_price(prices_list, price)
# 2. get_average_price(prices_list)
# 3. get_max_price(prices_list)

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)


# Then create a simple menu:
# 1 -> Add price
# 2 -> Show average price
# 3 -> Show highest price
# q -> Quit

prices = []

while True:

    print("\n1 -> Add price")
    print("2 -> Show average price")
    print("3 -> Show highest price")
    print("q -> Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)

    elif choice == "2":
        if len(prices) > 0:
            print("Average Price:", get_average_price(prices))
        else:
            print("No prices available.")

    elif choice == "3":
        if len(prices) > 0:
            print("Highest Price:", get_max_price(prices))
        else:
            print("No prices available.")

    elif choice.lower() == "q":
        break

    else:
        print("Invalid Choice")