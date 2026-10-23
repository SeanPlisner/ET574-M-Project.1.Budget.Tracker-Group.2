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
