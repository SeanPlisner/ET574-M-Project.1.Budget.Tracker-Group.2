def add_expense():
    print("\nAdd Expense")
    
    category = input("Enter the category of the expense: ")

    if catergory == "":
        print("Category cannot be empty. Please try again.")
        return