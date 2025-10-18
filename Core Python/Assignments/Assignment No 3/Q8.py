import random  


user = input("User ID: ")
pwd = input("Password: ")


if user == "admin" and pwd == "1234":
    
    code = random.randint(1000, 9999)
    print("Captcha:", code)

    
    entered = input("Type the captcha: ")
    if entered == str(code):
        print("Login successful!")
    else:
        print("Login failed! Captcha wrong.")
else:
    print("Wrong User ID or Password.")