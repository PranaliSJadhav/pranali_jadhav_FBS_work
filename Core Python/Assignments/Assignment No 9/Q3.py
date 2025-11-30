def revNo(n , rev = 0 ):
    
    if n == 0:
        return rev
    return revNo(n // 10 , rev * 10 + n % 10)

n = int(input("enter number :"))
print("reverse number is:", revNo(n))

