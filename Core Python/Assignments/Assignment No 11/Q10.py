lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []

for num in lst:
    if num % 2 != 0:
        new_list.append(num)

print("List after removing even numbers:", new_list)
