def add_num(*a):
    for i in a:
        print("items are listed")
        if i==type(str):
            print("enternd string is : ",i)
        elif i==type(int):
            print("entered item integer : ",i)
        elif i==type(float):
            print("enter item is float",i)
        else:
            print("its real number",i)
a=eval(input("enter your item "))
add_num(a)