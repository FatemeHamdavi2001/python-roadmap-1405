username = input("Enter your Username: ")
age = int(input("Enter your Age: "))
if age < 13 :
    print("Child")
elif 13 <= age <= 17 :
    print("Teenager")
elif 18 <= age <= 59 :
    print("Adult")
else:
    print("Senior")

if username.startswith(("admin", "Admin")) :
    print("Admin account detected.")