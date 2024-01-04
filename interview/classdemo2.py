class EMP:
    rase_amount = 7.5

    def __init__(self, sal, name):
        self.sal = sal
        self.name = name

    def increse_amount(self):
        self.sal = self.sal + (self.sal * EMP.rase_amount / 100)

    def display(self):
        print("name: ", self.name, "salary: ", self.sal)


a = int(input("enter sallary"))
b = input("input name of emploay")
e1 = EMP(a, b)
e1.display()

print("after salary incressing")
e1 = EMP(5000, "amit")
e1.increse_amount()
e1.display()
