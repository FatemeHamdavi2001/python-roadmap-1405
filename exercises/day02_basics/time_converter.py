secound = int(input("Enter Secound: "))
hour = secound // 3600
Reminder = secound % 3600
minute = Reminder // 60
sec = Reminder % 60
print(hour,"hour\n",minute,"minute\n",sec,"secounds")