def is_prime(n, d=2):
    if n <= 1:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

n = int(input("Enter number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")