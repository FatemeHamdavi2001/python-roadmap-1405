base_salary = float(input("please Enter your Base salary: "))
overtime_hours =float(input("please Enter Over time Hours: "))
overtime_rate = float(input("please Enter Over time rate: "))
final_salary = base_salary + (overtime_hours * overtime_rate)
if (final_salary > 200000000) : 
    {
        print("Salary = ", final_salary," ; High salary")
    }
else :
    {
        print("Salary = ", final_salary," ; Normal salary")
    }