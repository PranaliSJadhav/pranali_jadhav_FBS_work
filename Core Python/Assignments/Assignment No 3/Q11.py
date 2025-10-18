ticket = float(input("Enter ticket price per person: "))

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

# person 1
if age1 < 12:
    amt1 = ticket * 0.7
elif age1 > 59:
    amt1 = ticket * 0.5
else:
    amt1 = ticket

# person 2
if age2 < 12:
    amt2 = ticket * 0.7
elif age2 > 59:
    amt2 = ticket * 0.5
else:
    amt2 = ticket

# person 3
if age3 < 12:
    amt3 = ticket * 0.7
elif age3 > 59:
    amt3 = ticket * 0.5
else:
    amt3 = ticket

# person 4
if age4 < 12:
    amt4 = ticket * 0.7
elif age4 > 59:
    amt4 = ticket * 0.5
else:
    amt4 = ticket

# person 5
if age5 < 12:
    amt5 = ticket * 0.7
elif age5 > 59:
    amt5 = ticket * 0.5
else:
    amt5 = ticket

# total amount
total = amt1 + amt2 + amt3 + amt4 + amt5
print("Total ticket amount =", total)

