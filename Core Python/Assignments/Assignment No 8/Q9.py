def palindrome(n):
    original = n
    rev = 0
    while(n > 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if(rev == original):
        print('it is a palindrome number')
    else:
        print('it is not a palindrome number')

num = int(input("enter number : "))
result = palindrome(num)
print(result)