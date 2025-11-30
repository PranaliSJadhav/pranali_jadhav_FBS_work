def armstrong(num):
    t = num
    total = 0
    count = 0

    t = num
    while( t > 0):
          count += 1
          t //= 10
        
    t = num
    while( t  > 0):
          digit = t % 10
          total = total + digit ** count
          t //= 10
    if(total == num):
            print("It is a armstrong number..")
    else:
            print("It is not a armstrong number..")

num = int(input("enter a number : "))
armstrong(num)