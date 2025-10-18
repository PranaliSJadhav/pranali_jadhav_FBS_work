n = int(input("enter a three digit number"))

digit1 = n // 100
digit2 = (n //10)  % 10
digit3 = n % 10

sum = digit1 + digit2 + digit3

print("the sum of three digit number is",sum)