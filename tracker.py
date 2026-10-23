from data import categories, amounts, descriptions


def add_expense():
    print("\nAdd Expense")
    
    category = input("Enter the category of the expense: ")

    if catergory == "":
        print("Category cannot be empty. Please try again.")
        return

    amount = input("Enter the amount of the expense: ")

    try:
        amount = float(amount)

        if amount <= 0:
            print("Amount must be greater than zero. Please try again.")
            return

    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    amount_text  =("Enter the amount of the expense: ")

    try:
        amount = float(amount_text)

        if amount <= 0:
            print("Amount must be greater than zero. Please try again.")
            return

    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    description = input("Enter a description for the expense: ")

    if description == "":
        print("Description cannot be empty. Please try again.")
        return

    categories.append(category)
    amounts.append(amount)
    descriptions.append(description)

    print("\nExpense added successfully!")

def view_all_expenses():
    print("\nAll Expenses:")
    
    if (len(categories)) == 0:
        print("No expenses recorded.")
        return

    for i in range(len(categories)):
        print("\n Expense", i +1)
        print("Category:", categories[i])
        print("Amount: $", format(amounts[i], ".2f"))
        print("Description:", descriptions[i])
