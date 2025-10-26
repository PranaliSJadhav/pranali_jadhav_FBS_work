userid = "admin"
passwoord = "4567"

for i in range(3):
    user = input("enter user id:")
    p = input("enter password:")
    if user == userid and p == passwoord:
        print("Login successful.")
        break
    else:
        print("Invalid credentials,try again")
else:
    print("3 attempts over. program terminated")


