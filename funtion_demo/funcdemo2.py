import math
def circle(radius):
    def area():
        a=math.pi*math.pow(2,radius)
        print(a)
    def circumferance():
        a=math.tau*radius
        print(a)
    area()
    circumferance()
a=int(input("enter the length"))
circle(a)

