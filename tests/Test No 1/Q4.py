length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

area = (length * breadth) + (0.5 * 3.14 * radius * radius)
perimeter = (2 * breadth) + length + (3.14 * radius)

print("Area of figure =", area)
print("Perimeter of figure =", perimeter)
