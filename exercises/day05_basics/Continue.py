negative_count = 0
for i in range(10):
    number = int(input())
    if number == 0:
        continue
    if number < 0:
        negative_count += 1
print("Negative Count:", negative_count)