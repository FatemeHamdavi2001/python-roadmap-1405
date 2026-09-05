username = input("Enter Username:")
age = int(input("Enter Age:"))
password = input("Enter Password:")
#username check
userstart = username.startswith(("admin", "Admin"))
if userstart:
    account_type = "Admin"
else:
    account_type = "User"
#age check
if age < 13:
    age_group = "Child"
elif 13 <= age <= 17:
    age_group = "Teenager"
elif 18 <= age <= 59:
    age_group = "Adult"
else:
    age_group = "Senior"
#password check
digit = 0
alpha = 0
for i in range(len(password)) :
    char = password[i]
    if char.isdigit() :
        digit += 1
    if char.isalpha() :
        alpha += 1
        
if len(password) >= 8 and digit >= 1 and alpha >= 1:
    pwd_strength = "High"
    risk_level = "Safe"
elif len(password) >= 8 and (digit >= 1 or alpha >= 1):
    pwd_strength = "Medium"
    risk_level = "Review Required"
else:
    pwd_strength = "Low"
    risk_level = "Action Required"
#print result
print("\n--- Account Report ---\n")
print(f"Account type: {account_type}")
print(f"Age group: {age_group}")
print(f"Password strength: {pwd_strength}\n")
print(f"Risk level: {risk_level}")