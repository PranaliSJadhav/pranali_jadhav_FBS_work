s = input("Enter a string: ")

char_count = 0
word_count = 1   

for ch in s:
    char_count += 1
    if ch == " ":
        word_count += 1


if char_count == 0 or s.strip() == "":
    word_count = 0

print("Number of characters:", char_count)
print("Number of words:", word_count)
