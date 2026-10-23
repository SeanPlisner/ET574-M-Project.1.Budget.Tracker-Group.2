from tracker import add_expense, summary_report, view_all_expenses


print("Welcome to Budget Tracker!")

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. View All Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        summary_report()

    elif choice == "3":
        view_all_expenses()

    elif choice == "4":
        print("\nExiting the program. Bye!")
        break

    else:
        print("\nInvalid choice. Please try again. Select 1, 2, 3, or 4.")
