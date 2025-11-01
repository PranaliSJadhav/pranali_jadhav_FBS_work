for i in range(1,5):
    print(' '*(4-i),end = ' ')
    k = 1
    for j in range(1,i+1):
        print(k,end = ' ')
        k = k * (i - j) // j
    print()