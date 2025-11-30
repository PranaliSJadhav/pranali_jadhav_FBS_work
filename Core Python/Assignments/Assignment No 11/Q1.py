lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []
odd = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("The even list:", even)
print("The Odd list:", odd)
