lst = [15,30,27,25,45,40,45]

m = int(input("enter a 1st number :"))
n = int(input("enter a 2nd number :"))

new_list = []

for i in lst:
    if i % m == 0 and i % n == 0:
        new_list.append(i)

print("new list is :", new_list)