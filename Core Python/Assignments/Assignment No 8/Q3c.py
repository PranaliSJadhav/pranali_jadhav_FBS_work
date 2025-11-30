def sum_of_power(n):
    if(n <= 0):
        return 0
    total = 0
    for i in range(1,n+1):
        t = i ** i
        total = total + t
    return total

n = int(input("enter number :"))
result = sum_of_power(n)
print(result)
