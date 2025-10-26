# Program to find sum of factorials: 1! + 2! + 3! + ... + n!

n = int(input("Enter n: "))
total = 0
fact = 1

for i in range(1, n + 1):
    fact *= i         
    total += fact     

print("Sum of factorials up to", n, "=", total)
