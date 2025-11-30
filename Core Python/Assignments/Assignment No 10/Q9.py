lst = [2, 3, 5, 8, 4, 9]

even_lst = []
odd_lst = []

for i in lst:
    if i %2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
    

print("Even list :", even_lst)
print("Odd list :", odd_lst)