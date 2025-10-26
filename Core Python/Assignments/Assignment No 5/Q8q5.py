
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))
S = 0

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)
    S += term if i % 2 != 0 else -term  # Add if odd, subtract if even

print("Sum of the series =", S)
