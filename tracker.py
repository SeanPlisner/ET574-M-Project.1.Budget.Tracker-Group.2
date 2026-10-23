from data import categories, amounts, descriptions



def add_expense():
    print("\nAdd Expense")
    
    category = input("Enter the category of the expense: ")

    if category == "":
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


def summary_report():
    print("\nSummary Report:")
    
    if len(amounts) == 0:
        print("No expenses recorded.")
        return

    total = sum(amounts)
    number_of_expenses = len(amounts)
    average = total / number_of_expenses
    highest = max(amounts)
    lowest = min(amounts)

    print("Total Expenses: $", format(total, ".2f"), sep="")
    print("Number of Expenses:", number_of_expenses)
    print("Average Expense: $", format(average, ".2f"), sep="")
    print("Highest Expense: $", format(highest, ".2f"), sep="")
    print("Lowest Expense: $", format(lowest, ".2f"), sep="")
