expenses = []

print("Daily Expense Tracker")

for i in range(3):
    amount = int(input("Enter expense amount: "))
    expenses.append(amount)

total = sum(expenses)

print("\nExpenses:", expenses)
print("Total Spent: ₹", total)

if total > 500:
    print(" You spent a lot today!")