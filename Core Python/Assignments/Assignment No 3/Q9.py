print("Enter marks for 5 subjects (0 to 100):")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

# Calculate total and average percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Decide grade using simple if-elif-else branching
if percentage >= 75:
    print("You got Distinction!")
elif percentage >= 60:
    print("You got First Class!")
elif percentage >= 50:
    print("You got Second Class!")
elif percentage >= 35:
    print("You passed!")
else:
    print("You failed!")

# Show percentage too
print(f"Your percentage is: {percentage:.2f}%")