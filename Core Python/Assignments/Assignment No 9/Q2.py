def countDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def armStrong(num):
    digits = countDigits(num)   
    total = 0
    original = num

    while num > 0:
        d = num % 10
        total = total + (d ** digits)
        num //= 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


n = int(input("Enter a number: "))
armStrong(n)
