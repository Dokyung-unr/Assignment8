
expenses = []


def add_expense():
    name = input("What did you buy? ")

    if name == "":
        print("Please enter an item name.")
        return

    # Check that the price is a valid positive number.
    try:
        price = float(input("How much? "))
    except ValueError:
        print("Please enter a valid price.")
        return

    if price <= 0:
        print("Price must be greater than zero.")
        return

    # Save the item name and price together.
    expenses.append((name, price))
    print("Added!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print("Your expenses:")

    for name, price in expenses:
        print(f"{name} ${price:.2f}")


def view_total():
    total = 0

    # Add each expense to calculate the total.
    for name, price in expenses:
        total += price

    print(f"Total expenses: ${total:.2f}")


# Keep showing the menu until the user chooses Exit.
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Wrong option")
