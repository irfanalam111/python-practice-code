def circle(radius, pi=3.14):
    circumferance = 2 * pi * radius
    area = pi * radius ** 2
    print(circumferance, area)


a = int(input('enter radius'))
circle(a)
