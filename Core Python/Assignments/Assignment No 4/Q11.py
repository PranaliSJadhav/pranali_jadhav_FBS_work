n = int(input("Enter number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    
    # calculate factorial manually
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    
    sum += fact
    temp //= 10

if sum == n:
    print(n, "is a Strong Number")
else:
    print(n, "is not a Strong Number")
