class Student:
    def __init__(self, studentId=0, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 40:
            return "Pass"
        else:
            return "Fail"


class MedicalStudent(Student):
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 specialization="", internshipMarks=0):
        super().__init__(studentId, name, age, percentage)   # ✅ FIXED
        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.internshipMarks = int(input("Enter Internship Marks: "))

    def calculateRank(self):
        total = (self.percentage + self.internshipMarks) / 2
        if total >= 75:
            return "Distinction"
        elif total >= 60:
            return "First Class"
        elif total >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"{self.studentId} | {self.name} | "
                f"Specialization: {self.specialization} | "
                f"Rank: {self.calculateRank()}")



m1 = MedicalStudent()
m1.accept()
print(m1)