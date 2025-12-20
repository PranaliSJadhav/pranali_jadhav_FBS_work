class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        cm = self.cm + other.cm
        m = cm // 100
        cm = cm % 100

        m = m + self.m + other.m
        km = m // 1000
        m = m % 1000

        km = km + self.km + other.km

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    def __del__(self):
        print("Distance object destroyed")



d1 = Distance(2, 450, 75)
d2 = Distance(1, 600, 50)

print("Total Distance:", d1 + d2)
