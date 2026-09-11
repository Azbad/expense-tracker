# Expense Tracker - Edit Expense Feature
print("====    EXPENSE TRACKER    ====")

expenses = []


def add_expense():
    adding_expense = True

    while adding_expense:
        while True:
            expense = input("Enter expense name: ").strip()
            if not expense:
                print("name of expense cannot be empty")
                continue
            break
        while True:
            try:
                amount = int(input("Enter amount: "))
                if amount < 0:
                    print("Enter zero or greater")
                    continue
                break
            except ValueError:
                print("Invalid input,enter number only.")

        while True:
            category = input("Enter category: ").strip().lower()
            if not category:
                print("name of category cannot be empty")
                continue
            break

        expense_data = {
            "name": expense,
            "amount": amount,
            "category": category
        }

        expenses.append(expense_data)
        print("Expenses added successfully! ")
        print()

        while True:
            done = input("Record another expense,(yes/no)?: ").strip().lower()

            if done == "yes":
                break
            elif done == "no":
                adding_expense = False
                break
            else:
                print("Enter yes/no")


def view_expenses():
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']}")
        print(f"   {expense['amount']}")
        print(f"   {expense['category']}")
        print()

    if not expenses:
        print("No expenses recorded yet")


def calculate_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total expenses: {total}")
    print()


def search_expense():
    found = False
    cat_expense = input("Enter expense category: ").strip().lower()

    for expense in expenses:
        if cat_expense == expense['category']:
            if not found:
                print(f"Expenses in {expense['category']}: ")
            print(f"  {expense['name']} - {expense['amount']} ")
            found = True

    if not found:
        print("No expenses found in this category.")


def category_summary():
    cat_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in cat_totals:
            cat_totals[category] = amount
        else:
            cat_totals[category] = cat_totals[category] + amount

    if not cat_totals:
        print("No categories yet!")
        return

    print("====    CATEGORY SUMMARY    ====")

    for category, total in cat_totals.items():
        print(f"{category}: {total}")


def delete_expense():
    try:
        del_expense = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid input,enter number only.")
        return

    found = False

    for number, expense in enumerate(expenses, start=1):
        if number == del_expense:
            expenses.remove(expense)
            print("Expense removed successfully!")
            found = True
            break
    if not found:
        print("Invalid expense number")


while True:
    print("1. Add/record a new expense")
    print("2. View all existing expenses")
    print("3. Calculate total expenses")
    print("4. Search for expense")
    print("5. To calculate total expenses in each category")
    print("6. Remove expense")
    print("7. Exit")
    print()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        category_summary()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        break
    else:
        print("Invalid choice!")
