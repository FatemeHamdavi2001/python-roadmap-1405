n = int(input("Enter number:"))
for i in range(n, 0, -1):
    if i % 2 == 0 :
        continue
    if i == 3 :
        break
    print(i)