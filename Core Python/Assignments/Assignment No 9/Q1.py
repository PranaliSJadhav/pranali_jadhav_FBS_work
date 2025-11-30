def fact(n):
    if(n == 0):
       return 1
    elif(n < 0):
        return f'{n} is a negative number'
    else:
        return n * fact(n-1)
def sumOfFact(n):
    if(n == 1):
        return 1
    return n * fact(n-1)
 
n = int(input("Enter a number: "))
result = fact(n)
print(result)
