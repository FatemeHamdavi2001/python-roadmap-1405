food = float(input("Enter food expense in month: "))
transport = float(input("Enter transport expense in month: "))
entertainment = float(input("Enter Entertainment expense in month: "))
other = float(input("Enter other expense in month: "))
total_expenses = food + transport + entertainment + other
income = float(input("Enter your income: "))
remaining = income - total_expenses
print("===== EXPENSE REPORT ====="
      "\nFood: ", food,
      "\nTransport: ", transport,
      "\nEntertainment: ", entertainment,
      "\nOther: ", other,

      "\nTotal: ", total_expenses,
      "\nRemaining: ", remaining,

     "\n==========================")
if remaining < 0 :
    print("Warning: Expenses exceed income.")
else :
    print("Budget status: OK")