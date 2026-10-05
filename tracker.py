# Project: Expense Tracker - Installment 2: Talking to the User
# Author: Paul Ulysses Macarilay
# Description: Shows the landing page, asks for two expenses, prints a summary.
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add Expense\t\t(coming soon)")
print("\t[2] View All Expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t-{item1}:\t${amount1:.2f}")
print(f"\t-{item2}: \t${amount2:.2f}")
print(f"Total spent: \t\t${total:.2f}")
print(f"Average: \t\t${average:.2f}")
print("Made by: Paul Ulysses Macarilay | Installment 2")
print("-" * 40)