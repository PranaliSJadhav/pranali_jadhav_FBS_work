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

    def __str__(self):
        return f"{self.studentId} | {self.name} | {self.percentage}% | Rank: {self.calculateRank()}"


class EnggStudent(Student):
    def __init__(self, studentId=0, name="", age=0, percentage=0.0,
                 branch="", internalMarks=0):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = int(input("Enter Internal Marks: "))

    def calculateRank(self):
        total = (self.percentage + self.internalMarks) / 2
        if total >= 75:
            return "Distinction"
        elif total >= 60:
            return "First Class"
        elif total >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"{self.studentId} | {self.name} | Branch: {self.branch} | "
                f"Rank: {self.calculateRank()}")



e1 = EnggStudent()
e1.accept()
print(e1)