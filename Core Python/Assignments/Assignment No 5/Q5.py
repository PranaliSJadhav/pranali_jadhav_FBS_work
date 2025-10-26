amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for n in notes:
    if amount >= n:
        count = amount // n
        amount %= n
        print(n, "x", count)
