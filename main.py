from data_manager import load_expenses, save_expenses
from expense_tracker import add_expense, show_expenses



def main():
    expenses = load_expenses()

    while True:
        print("\nMenu:")
        print("1. Log an expense")
        print("2. View all spend")
        print("3. Quit")
        choice = input("Your pick: ")

        if choice == "1":
            if add_expense(expenses):
                save_expenses(expenses)
                print("Done! Expense added.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Whoops! That's not right. Pick another.")


if __name__ == "__main__":
    main()
