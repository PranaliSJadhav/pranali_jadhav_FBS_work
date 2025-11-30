lst = [2 , 3 ,5, 6, 3, 2, 1, 9]
unique_lst = []
print("list before duplicate:", lst)

for i in lst:
    present = False


    for j in unique_lst:
        if i == j:
            present = True
            break

    if present == False:
        unique_lst.append(i)

print("list without duplicates:",unique_lst)

