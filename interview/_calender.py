import calendar

try:
    a = int(input("enter year name "))
    while True:
        if a <= 0:
            print("try again")
        ab = calendar.calendar(a)
        print(f"calender is{ab}")
        break
except Exception:
    pass
