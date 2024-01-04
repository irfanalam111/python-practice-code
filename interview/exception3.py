class NegatineValueError(Exception):
    pass


while (True):
    try:
        a = int(input("enter first number"))
        b = int(input("second number"))
        if a <= 0 or b < 0:
            raise NegatineValueError("negstive number is not allowed")
        c = a / b
        print("division is :", c)
        break
    except ValueError:
        print("strings are not allowed")
    except ZeroDivisionError:
        print("denominator should not be zero")
    except NegatineValueError as ex:
        print(ex)
