basic_salary = int(input("enter basic salary of an employee:"))

DA = 10/100 * basic_salary
TA = 12/100 * basic_salary
HRA = 15/100 * basic_salary
total_salary = basic_salary + DA + TA + HRA

print("the total salary of an employee is :",total_salary)