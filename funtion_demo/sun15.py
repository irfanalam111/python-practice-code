def shape(*a):
    for i in a:
        if i=="circle":
            print("thise shape is circle")
        elif i=="cylinder":
            print("this shape is cylinder")
        elif i=="cone":
            print("this shape is cone")
        elif i=="tringle":
            print("this shape is tringle")
        else:
            print("not a shape")
shape("circle","cone","cylinder","tringle","area")
