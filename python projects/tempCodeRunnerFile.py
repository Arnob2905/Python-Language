import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ExpenseTracker:
    def __init__(self):
        self.logs = []

    def add_expense(self, date, amount, category, description):
        if amount <= 0:
            print("Amount can't be zero or negative.")
            return
        allowed = ["food", "travel", "bills", "shopping", "others"]
        if category.lower() not in allowed:
            print(f"Invalid category: {category}")
            return

        self.logs.append({
            "date": date,
            "amount": amount,
            "category": category.lower(),
            "description": description
        })
        print("Entry saved.")

    def get_summary(self):
        if not self.logs:
            print("No entries to show.")
            return
        df = pd.DataFrame(self.logs)
        print("\n...Summary...")
        print("Total:", df["amount"].sum())
        print("Average:", df["amount"].mean())

    def filter_expenses(self, condition):
        try:
            df = pd.DataFrame(self.logs)
            result = df.query(condition)
            print("\n...Filtered...")
            print(result)
        except:
            print("Invalid filter condition.")

    def generate_report(self):
        if not self.logs:
           print("Nothing to analyze.")
           return
        df = pd.DataFrame(self.logs)
        print("\nCurrent DataFrame:")
        print(df)
        grouped = df.groupby("category")["amount"].sum()
        print("\n...Category Analysis...")
        print(grouped)


    def bar_chart(self):
        if not self.logs:
            print("No data to plot.")
            return
        df = pd.DataFrame(self.logs)
        data = df.groupby("category")["amount"].sum()
        sns.barplot(x=data.index, y=data.values, palette="magma")
        plt.title("Expenses by Category")
        plt.ylabel("Amount")
        plt.xlabel("Category")
        plt.tight_layout()
        plt.show()

    def pie_chart(self):
        if not self.logs:
            print("No data to plot.")
            return
        df = pd.DataFrame(self.logs)
        parts = df.groupby("category")["amount"].sum()

        sns.set_style("whitegrid")
        colors = sns.color_palette("pastel")  # Auto adjust for number of categories

        plt.pie(parts.values, labels=parts.index, autopct="%1.1f%%",
                colors=colors[:len(parts)], startangle=90)
        plt.title("Spending Distribution")
        plt.axis("equal")
        plt.tight_layout()
        plt.show()


tracker = ExpenseTracker()

while True:
    print("\n--- Welcome to Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Filter Expenses")
    print("4. Analyze by Category")
    print("5. Show Bar Chart")
    print("6. Show Pie Chart")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nEnter Expense Details:")
        d = input("Date (YYYY-MM-DD): ")
        try:
            a = float(input("Amount: "))
        except ValueError:
            print("Invalid amount.")
            continue
        c = input("Category (food/travel/shopping/bills/others): ").strip()
        desc = input("Description: ")
        tracker.add_expense(d, a, c, desc)
        print("Current logs (for debug):")
        print(tracker.logs)

    elif choice == "2":
        tracker.get_summary()

    elif choice == "3":
        cond = input("Enter filter condition (e.g.amount > 100): ")
        tracker.filter_expenses(cond)

    elif choice == "4":
        tracker.generate_report()

    elif choice == "5":
        tracker.bar_chart()

    elif choice == "6":
        tracker.pie_chart()

    elif choice == "0":
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice. Try again!")
                 