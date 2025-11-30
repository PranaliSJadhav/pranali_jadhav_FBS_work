lst = [2, 4, 5, 2, 4, 3, 2]

new_lst =[]
n = int(input("enter Duplicate number to remove from list : "))

for i in lst:
    if i != n:
        new_lst.append(i)
    
print("new list is : ", new_lst)