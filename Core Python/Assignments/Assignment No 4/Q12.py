start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end+1):
    sum_digits = 0
    n_digits = len(str(num))
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** n_digits  # calculate power directly
        temp //= 10
    
    if sum_digits == num:
        print(num, end=" ")
