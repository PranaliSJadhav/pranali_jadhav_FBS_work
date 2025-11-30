def area_of_circle(radius):
    area = 3.14 *  radius ** 2
    return area

radius = float(input("enter radius of circle : "))


result = area_of_circle(radius)
print("the area of circle is :" , result)