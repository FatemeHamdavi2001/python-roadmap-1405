n = int(input("Please chose Number(1-4):"))
match n :
    case 1:
        print("Start")
    case 2:
        print("Settings")
    case 3:
        print("Help")
    case 4:
        print("Exit")
    case _:
        print("Invalid option")
    