try:
    a = int(input("enter first number: "))
    b = int(input("enter second number"))
    c = a * b
    print("product of a and b is: ", c)
    d = a / b
    print("divsion of a and b is: ", d)
    e = a + b
    print("addition of a and b is: ", e)
except ValueError:
    print("enter only integer")
except ZeroDivisionError:
    print("cannot should be denimonater is zero")
