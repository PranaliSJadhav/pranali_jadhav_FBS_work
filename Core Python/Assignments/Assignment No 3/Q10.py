gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print("Eligible to marry.")
    else:
        print("Not eligible to marry.")
elif gender == "female":
    if age >= 18:
        print("Eligible to marry.")
    else:
        print("Not eligible to marry.")
else:
    print("Invalid gender entered.")