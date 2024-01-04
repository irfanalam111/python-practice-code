import math


class circle:
    def __init__(self, r):
        self.r = r

    def circ__(self):
        circ = math.tau * math.pow(self.r, 2)
        print("circ is", circ)

    def area(self):
        area = math.pi * math.pow(self.r, 2)
        print(area)
    def __str__(self):
        return f"area {self.area()}, circumferance {self.circ__()}"


e1 = circle(10)

