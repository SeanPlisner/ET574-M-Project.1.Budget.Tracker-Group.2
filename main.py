print("Welcome to Budget Tracker!")

choice = ""

while choice != "4":
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. View All Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAdd expense selected")

    elif choice == "2":
        print("\nViewing summary selected")

    elif choice == "3":
        print("\nViewing all expenses selected")

    elif choice == "4":
        print("\nExiting the program. Bye!")

    else:
        print("\nInvalid choice. Please try again. Select 1, 2, 3, or 4.")