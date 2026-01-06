def Calculator():
    try:
        num1 = float(input("enter first input :"))
        num2 = float(input("enter second input : "))
        op = input("enter operator (+,-,*,/):")

        if (op == '+'):
            result = num1 +num2
        elif(op == '-'):
            result = num1 - num2
        elif(op == '*'):
            result = num1 * num2
        elif(op == '/'):
            result = num1 /num2
        else:
            raise ValueError("invalid operator")
        
        print("Result:",result)
    
    except ValueError as ve:
        print("Error:",ve)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed ")
    except Exception:
        print("Unknown error occured")

Calculator()