li = []

for i in range(9, -1, -1):
    sub_li = []

    for j in range(i * 10 + 1, (i * 10) + 11):
        sub_li.append(j)

    if (i % 2 != 0):
        sub_li.reverse()

    li = li + [sub_li]

print(li)
