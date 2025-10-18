a = float(input("enter angle 1:"))
b = float(input("enter angle 2:"))
c = float(input("enter angle 3:"))

if a == b == c:
    print("this is an equilateral triangle")
elif (a == b) or (a == c) or (b == c):
    print("this is an isoscales triangle")
else:
    print("this is an scalence triangle")