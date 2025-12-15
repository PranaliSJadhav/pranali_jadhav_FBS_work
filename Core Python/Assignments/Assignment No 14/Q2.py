def intersection(set1, set2):
    return set2 - set1.intersection(set2)  


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}


result = intersection(set1, set2)
print("Elements after remove intersection:", result)

