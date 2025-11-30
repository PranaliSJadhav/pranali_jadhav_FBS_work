def rev_no(n):
    rev = 0
    while(n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

num = int(input("enter number : "))
result = rev_no(num)
print(result)