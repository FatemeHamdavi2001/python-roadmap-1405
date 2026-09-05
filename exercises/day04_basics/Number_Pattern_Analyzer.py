n = int(input("Enter Number: "))
for i in range(1, n + 1) :
    if i % 2 == 0 and i % 3 == 0 :
        print(f"{i} → Even / Multiple of 3")
    elif i % 3 == 0 :
        print(f"{i} → Odd / Multiple of 3")
    elif i % 2 == 0 :
        print(f"{i} → Even")
    else:
        print(f"{i} → Odd")