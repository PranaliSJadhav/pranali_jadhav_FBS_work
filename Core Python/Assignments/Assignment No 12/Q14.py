s = input("Enter a string: ")

words = s.split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(count)