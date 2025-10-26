n = int(input("Enter number of passengers: "))
cost = float(input("Enter ticket cost per person: "))

total = 0  
for i in range(n):
    age = int(input(f"Enter age of passenger {i+1}: "))

    if age < 12:
        fare = cost * 0.7   
    elif age > 59:
        fare = cost * 0.5   
    else:
        fare = cost         

    total += fare

print("Total ticket amount to pay:",total)