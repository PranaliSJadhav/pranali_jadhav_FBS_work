li = [21,23,98,67,56,87,23,21,20,2,5,3]
num = int(input("enter number to check in list:"))
count = 0

for items in li:
    if(items == num):
      count += 1

if(count > 0 ):
    print("number present in list")
    print(f'{count} times it is present in the list.')
else:
    print("number not present in list")