correct = "123456Aa"
for i in range(5):
    password = input("Enter your password:")
    if password == correct:
        print("Access granted")
        break
else:
    print("Access denied")