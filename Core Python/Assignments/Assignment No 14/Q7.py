def find_missing(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    return missing_in_set2, missing_in_set1


set1 = {1, 2, 3, 4, 7}
set2 = {2, 3, 5, 6}
print(find_missing(set1, set2))
