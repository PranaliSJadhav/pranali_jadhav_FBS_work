def leap_year(year):
    if(year % 4 == 0):
        print("it is a leap year...")
    else:
        print("it is not a leap year...")

year = int(input("Enter a year : "))
leap_year(year)