class Student:
    def __init__(self, studentId=0, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f"{self.studentId} | {self.name} | {self.age} | {self.percentage}%"


class College:
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print("Student added successfully")
        else:
            print("College is full")

    def getStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                return s
        return None

    def removeStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                self.students.remove(s)
                print("Student removed")
                return
        print("Student not found")

    def __str__(self):
        result = "College Students:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result


c = College(2)

s1 = Student(1, "Amit", 20, 70)
s2 = Student(2, "Neha", 21, 82)

c.addStudent(s1)
c.addStudent(s2)

print(c)

c.removeStudent(1)
print(c)