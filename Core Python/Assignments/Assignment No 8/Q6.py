def fibonacci(n):
    if(n<=0):
       return 0
    a,b = 1,1
    
    print(a,b , end = ' ')
    for i in range(2,n):
      c = a+b
      print(c , end = ' ')
      a = b
      b = c

n = int(input("enter number :"))
result = fibonacci(n)  
print(result)