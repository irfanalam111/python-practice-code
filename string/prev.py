import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def circumferance(self):
        circ=math.tau*self.radius
        return circ
    def area(self):
        area=math.pi*math.pow(self.radius,2)
        return area
    def __str__(self):
        return f"area of circle:{self.area()}circumferance of circle: {self.circumferance()}"
class clynder(circle):
    def __init__(self,radius,height):
        self.height=height
        super().__init__(radius)
    def circumferance(self):
         return math.tau*self.radius*self.height
c=circle(12)
b=clynder(45,12)
print(c,b)

