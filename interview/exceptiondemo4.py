class NegativeValueError(Exception):
    pass


while (True):
    try:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        if a <= 0 or b < 0:
            raise NegativeValueError("negative value is not allowed")
        c = a / b
        print("Division is: ", c)
    except ValueError:
        print("strings are not allowed")
    except ZeroDivisionError:
        print("denimonater should not be zero")
    except NegativeValueError as ex:
        print(ex)
    else:
        break
