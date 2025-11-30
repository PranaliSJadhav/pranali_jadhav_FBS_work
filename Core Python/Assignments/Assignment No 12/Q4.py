s = input("Enter a string: ")

if len(s) > 1:
    first = s[0]
    last = s[-1]
    middle = s[1:-1]
    new_string = last + middle + first
else:
    new_string = s

print("New string:", new_string)