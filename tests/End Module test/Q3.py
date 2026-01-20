def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def binary_search(lst, key):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == key:
            return mid
        elif key < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Unsorted List:", lst)


selection_sort(lst)
print("Sorted List:", lst)

key = int(input("Enter element to search: "))

result = binary_search(lst, key)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")
