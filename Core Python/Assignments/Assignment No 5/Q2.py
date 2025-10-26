# Q2
n = int(input("Enter number of students: "))
total = 0

for i in range(n):
    print("\nStudent", i+1)
    marks = 0
    for j in range(5):
        m = int(input(f"Enter marks of subject {j+1}: "))
        marks += m
    per = marks / 5
    print("Percentage:", per)
    total += per

avg = total / n
print("\nAverage Percentage of all students:", avg)
