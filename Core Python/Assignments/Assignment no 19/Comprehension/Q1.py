numbers = [n for sub in [[i for i in range(1, 1001)]]
           for n in sub if n % 8 == 0]

print(numbers)