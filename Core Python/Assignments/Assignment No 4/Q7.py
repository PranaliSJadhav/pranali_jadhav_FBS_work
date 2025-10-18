n = int(input("Enter number: "))

for i in range(1, n+1):
    if i % 2 != 0:
        if i % 3 != 0:
            print(i, end=" ")
