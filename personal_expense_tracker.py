import os

def load_expenses(file_name):
    """Load expenses from a file."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            expenses = {}
            for line in lines:
                category, amount = line.strip().split(':')
                expenses[category] = expenses.get(category, 0) + float(amount)
            return expenses
    return {}

def save_expenses(file_name, category, amount):
    """Save an expense to the file."""
    with open(file_name, 'a') as file:
        file.write(f"{category}:{amount}\n")

def display_expenses(expenses):
    """Display all expenses."""
    print("\n--- Expense Summary ---")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print("----------------------\n")

def main():
    print("Welcome to the Personal Expense Tracker!")
    file_name = "expenses.txt"
    expenses = load_expenses(file_name)

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            category = input("Enter expense category (e.g., Food, Travel): ")
            try:
                amount = float(input(f"Enter amount spent on {category}: $"))
                expenses[category] = expenses.get(category, 0) + amount
                save_expenses(file_name, category, amount)
                print(f"Added ${amount:.2f} to {category}.")
            except ValueError:
                print("Invalid amount. Please try again.")

        elif choice == '2':
            display_expenses(expenses)

        elif choice == '3':
            print("Thank you for using the Personal Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

main()
