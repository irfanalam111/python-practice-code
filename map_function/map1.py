def mont_(my_string):
    if len(my_string)%2==0:
        print("even")
    else:
        print(my_string[0])
month=["january","february","march","april"]
a=map(mont_,month)
print(list(a))