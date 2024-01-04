def input_(a):
    for i in a:
        if i%2==0:
            print("squire of every even no. : ",i**2)
        else:
            print("its even : ")
a=list(input("enter your number : "))
b=map(input_,a)
print(list(b))
