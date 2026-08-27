email = input("Enter email: ")
index = email.find("@")
print("Username: ", email[:index])
print("Domain: ", email[index:])