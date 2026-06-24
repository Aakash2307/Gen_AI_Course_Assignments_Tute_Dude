# Task 3: User Menu (while loop + break/continue)

# 1. Implement a simple while-loop driven menu that keeps asking the user
# to choose an action until they press q to quit.

orders = []

while True:

    print("\nMenu")
    print("1 - Add order amount")
    print("2 - Show all orders")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter order amount: "))
        orders.append(amount)

    elif choice == "2":
        total = 0

        print("\nOrders:")

        for order in orders:

            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0

            final_amount = order - ((order * discount) / 100)

            print("Original:", order, "Final:", final_amount)

            total += final_amount

        print("Total:", total)

    elif choice == "q":
        break

    else:
        print("Invalid input.")
        continue