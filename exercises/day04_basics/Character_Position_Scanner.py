string = input("Enter String:")
for i in range(len(string)) :
    char = string[i]
    if char.isalpha() :
        print(f"Position {i} → {char} → Letter")
    elif char.isdigit() :
        print(f"Position {i} → {char} → Number" )
    elif char.isspace() :
        print(f"Position {i} → {char} → Space")
    else:
        print(f"Position {i} → {char} → Other")