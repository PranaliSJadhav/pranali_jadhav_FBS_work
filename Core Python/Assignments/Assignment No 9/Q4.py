def sum_list(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_list(arr, n-1)

n = int(input("How many numbers? "))
arr = []
for i in range(n):
    arr.append(int(input("Enter number: ")))

print("Sum =", sum_list(arr, n))