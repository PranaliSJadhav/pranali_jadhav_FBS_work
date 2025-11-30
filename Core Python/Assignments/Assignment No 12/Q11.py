s = input("Enter a string: ")
new_s = ""

for ch in s:
    if ch == " ":
        new_s += "-"
    else:
        new_s += ch

print(new_s)