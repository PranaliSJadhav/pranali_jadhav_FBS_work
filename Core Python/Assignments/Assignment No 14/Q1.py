def find_difference(set1, set2):
    return set1 - set2   


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}


result = find_difference(set1, set2)
print("Elements in set1 not in set2:", result)

