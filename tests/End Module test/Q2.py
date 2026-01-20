import random


snake_heads = random.sample(range(2, 100), 7)

print("---SNAKE BOARD---\n")

for row in range(10):
    start = 100 - row * 10
    end = start - 10

  
    if row % 2 == 0:
        numbers = range(start, end, -1)
    else:
        numbers = range(end + 1, start + 1)

    for num in numbers:
        if num in snake_heads:
            print(" >", end=" ")
        else:
            print(f"{num:2}", end=" ")
    print()
