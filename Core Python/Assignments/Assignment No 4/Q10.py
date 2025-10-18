n = int(input("Enter number: "))
div = 0

for i in range(1, n):
    if n % i == 0:
        div += i

if div == n:
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")
