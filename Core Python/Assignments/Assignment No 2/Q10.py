n = int(input("enter three digit number"))

last_digit = n%10
middle_digit = (n // 10) % 10
first_digit = n//100

rev = (last_digit * 100) + (middle_digit * 10) + (first_digit)
print("the reversed number is :",rev) 