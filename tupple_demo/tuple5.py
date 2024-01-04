def my_tuple(a,b,c,d):
    ab=a+b+c+d
    cd=a*b*c*d
    return cd,ab
my_tuple2=(12,45,23,67)
x=my_tuple(*my_tuple2)
a,b=x
print(a,b)