import json
from datetime import datetime

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
    for i, exp in enumerate(expenses, start = 1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} uah | {exp['comment']}")


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
