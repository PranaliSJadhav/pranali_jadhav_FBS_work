n = int(input("enter n:"))
total = 0
fact =1 

for i in range(1 , n+1):
    fact *= i
    total += fact

print("the sum of factorial up to",n, '=' , total)