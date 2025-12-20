from SY.SYMarks import SYMarks
from TY.TYMarks import TYMarks


class Student:
    def __init__(self, roll, name, sy_marks, ty_marks):
        self.roll = roll
        self.name = name
        self.sy_marks = sy_marks   
        self.ty_marks = ty_marks  

    def calculate_grade(self, percentage):
        if percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        total_marks = self.sy_marks.total() + self.ty_marks.total()
        max_marks = 500   
        percentage = total_marks / max_marks * 100
        grade = self.calculate_grade(percentage)

        print("------ Student Result ------")
        print("Roll No:", self.roll)
        print("Name:", self.name)
        print("Total Marks:", total_marks)
        print("Percentage:", round(percentage, 2))
        print("Grade:", grade)


sy = SYMarks(70, 65, 75)
ty = TYMarks(72, 80)

student = Student(1, "Sarswati", sy, ty)
student1 = Student(2,"Parvati", sy, ty )
student.display_result()
student1.display_result()