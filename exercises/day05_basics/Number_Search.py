target = int(input("Please Enter target number: "))
for i in range(5) :
    number = int(input())
    if number == target :
        break
else:
    print("target number not found")