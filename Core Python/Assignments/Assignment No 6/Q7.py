for i in range(1,6):
    for j in range(5,i,-1):
          print(' ',end=' ')
    for j in range(65,64+2*i):
        print(chr(j),end=' ')
    print()