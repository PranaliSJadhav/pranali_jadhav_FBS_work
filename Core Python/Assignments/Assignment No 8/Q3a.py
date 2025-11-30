def sum_of_series(n):
    if(n >=1):
        sum = n * (n+1) // 2
        return sum
    
n = int(input("enter a value:"))

result = sum_of_series(n)
print(result)