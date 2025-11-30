lst = ["apple", "kiwi", "banana", "fig", "cherry"]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if len(lst[i]) > len(lst[j]):
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted by length:", lst)
