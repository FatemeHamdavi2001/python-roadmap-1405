first_name = input("First name:")
last_name = input("Last_name:")
birth_year = int(input("Birth year:"))
username = first_name.lower() + '_' + last_name.lower() + str(birth_year)
full_name = first_name + " " + last_name
print("===== Username Analyzer ====="
      "\nName:", full_name,
      "\nUsername:", username,
      
      "\nFirst character:", full_name[0],
      "\nLast character:", full_name[-1],
      
      "\nName length:", len(full_name)
     )
if len(username) > 15 :
    print("Username status: Long")
else :
    print("Username status: OK")