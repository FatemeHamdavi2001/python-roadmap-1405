username = "admin"
password = "1234"
for i in range(5):
    inputuser = input("Enter username:")
    inputpass = input("Enter password:")
    if inputuser == username and inputpass == password :
        print("Login successful")
        break
    elif inputuser != username :
        print("Unknown user")
    elif inputpass != password :
        print("Wrong password")
else:
    print("Account locked")
        