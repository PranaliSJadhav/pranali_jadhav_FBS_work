side1 = float(input("enter side 1 of angle1 :"))
side2 = float(input("enter side 2 of angle1 :"))
side3 = float(input("enter side 3 of angle1 :"))

if (side1 + side2 > side3):
    if (side1 + side3 > side2):
        if(side2 + side3 > side1):
            print("triangle is valid:")
        else:
            print("triangle is not valid")
    else:
        print("triangle is valid") 
else:
    print("triangle is invalid")               


