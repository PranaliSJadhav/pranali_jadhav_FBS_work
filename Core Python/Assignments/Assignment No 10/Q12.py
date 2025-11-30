lst = [2,4,3,7,6,9,8]

sq_lst = []
cube_lst = []
for i in lst:
    square = i ** 2
    sq_lst.append(square)

    cube = i ** 3
    cube_lst.append(cube)

print("the list of squares is :" , sq_lst)
print("the list of cubes is :", cube_lst)