class Time:
    def __init__(self,h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self,second):
        sec = self.s + second.s
        min = self.m + second.m
        hr = self.h + second.h

        if sec >= 60:
            min += sec // 60
            sec = sec % 60

        if min >= 60:
            hr += min//10
            min = min % 60
    
        return Time(hr, min, sec)

    def display(self):
        print(f"{self.h}:{self.m}:{self.s}")


h1 = int(input("Enter hours: "))
m1 = int(input("Enter Minutes: "))
s1 = int(input("enter Seconds: "))

t1 = Time(h1, m1, s1)


h2 = int(input("Enter hours: "))
m2 = int(input("Enter Minutes: "))
s2 = int(input("enter Seconds: "))

t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("Addition od 2 time zone is: ")

t3.display()

