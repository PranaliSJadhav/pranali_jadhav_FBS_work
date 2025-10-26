N = int(input("Enter N: "))
total = 0

for i in range(1, N + 1):
    total += N ** i

print("Sum of the series =", total)
