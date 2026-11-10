
expenses = []

def add_expense():
    name = input("What did you buy? ")
    price = input("How much? ")
    expenses.append(name + " $" + price)
    print("Added!")

def view_expenses():
    print("Your expenses:")
    for item in expenses:
        print(item)

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Wrong option")
