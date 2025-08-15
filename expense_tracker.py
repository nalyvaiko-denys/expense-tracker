from datetime import datetime, timedelta


def add_expense(expenses):
    try:
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
        return True
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return False


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

    today = datetime.now()

    if choice == "1":
        filtered_expenses = expenses
    elif choice == "2":
        month_str = input("Enter month (YYYY-MM): ")
        for exp in expenses:
            if exp['date'].startswith(month_str):
                filtered_expenses.append(exp)
    elif choice == "3":
        try:
            days = int(input("Enter number of days: "))
            limit_date = today - timedelta(days = days)
            for exp in expenses:
                expense_date = datetime.strptime(exp['date'], "%Y-%m-%d %H:%M:%S")
                if expense_date >= limit_date and expense_date <= today:
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
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']} uah | {exp['comment']}")
        total_amount += exp['amount']

    print(f"\nTotal spent in this period: {total_amount:.2f} uah")