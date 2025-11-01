for i in range(1, 6):
    for j in range(1, 11):
        if j <= i:
            print(j, end=' ')
        elif j > 10 - i:
            print(11 - j, end=' ')
        else:
            print(' ', end=' ')
    print()
