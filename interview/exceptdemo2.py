while True:
    try:
        a = int(input("enter first number"))
        b = int(input("enter second number"))
        if a <= 0 or b < 0:
            raise Exception("negative number is allowed try again")
        c = a / b
        print("division is :", c)
        break
    except ValueError:
        print("not allowed string")
    except ZeroDivisionError:
        print("dominator should not be zero")
    except Exception as ex:
        print(ex)
