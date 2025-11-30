lst = [2, 3, 6, 4, 8, 6, 9, 4]

new_lst = []

for i in lst:
    if i % 2 != 0:
        new_lst.append(i)
    

print("new list is :", new_lst)