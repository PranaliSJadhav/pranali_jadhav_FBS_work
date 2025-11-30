def area_of_rectangle(length,width):
    area = length * width
    return area

length = float(input("enter length : "))
width =  float(input("enter width :"))

result = area_of_rectangle(length , width)
print("the area of rectangle is :" , result)