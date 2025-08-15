import json
from datetime import datetime,timedelta

DATA_FILE = "expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent = 1)


def add_expense(expenses):
    amount = float(input("Total spend: "))
    category = input("Category: ")
    comment = input("Add a quick note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expenses.append({
        "amount": amount,
        "category": category,
        "comment": comment,
        "date": date
    })
    save_expenses(expenses)
    print("Done! Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("Nothing on the books yet.")
        return
    print("\nHow would you like to view your expenses?")
    print("1. All expenses")
    print("2. By a specific month (e.g., 2023-08)")
    print("3. By a number of recent days (e.g., last 7 days)")
    choice = input("Your pick: ")

    filtered_expenses = []
    total_amount = 0.0

    if choice == "1":
        filtered_expenses = expenses
    elif choice == "2":
        month_str = input("Enter month (year-month): ")
        for exp in expenses:
            if exp['date'].startswith(month_str):
                filtered_expenses.append(exp)
    elif choice == "3":
        try:
            days = int(input("Enter number of days: "))
            limit_date = datetime.now() - timedelta(days = days)
            for exp in expenses:
                expense_date = datetime.strptime(exp['date'], "%Y-%m-%d %H:%M:%S")
                if expense_date >= limit_date:
                    filtered_expenses.append(exp)
        except ValueError:
            print("Invalid number of days. Showing all expenses.")
            filtered_expenses = expenses
    else:
        print("Invalid choice. Showing all expenses.")
        filtered_expenses = expenses

    if not filtered_expenses:
        print("No expenses found for this period.")
        return

    for i, exp in enumerate(filtered_expenses, start = 1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} uah | {exp['comment']} ")
        total_amount += exp['amount']

    print(f"\nTotal spent in this period: {total_amount:.2f} uah")


def main():
    expenses = load_expenses()

    while True:
        print("\nMenu:")
        print("1. Log an expense")
        print("2. View all spend")
        print("3. Quit")
        choice = input("Your pick: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Whoops! That's not right. Pick another.")


if __name__ == "__main__":
    main()
