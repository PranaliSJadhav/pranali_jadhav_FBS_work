s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

c1 = 0
for _ in s1:
    c1 += 1

c2 = 0
for _ in s2:
    c2 += 1

if c1 > c2:
    print("Larger string:", s1)
elif c2 > c1:
    print("Larger string:", s2)
else:
    print("Both strings are equal")