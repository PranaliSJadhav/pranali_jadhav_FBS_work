def sum_of_fact(n):
    if(n < 1):
        return 0
    total = 0
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
        total = total + fact
    return total 

n = int(input("enter a value:"))

result = sum_of_fact(n)
print(result)