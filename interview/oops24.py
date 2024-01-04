class person:
    def __init__(self, age, gender, name, sal):
        self.age = age
        self.gender = gender
        self.name = name
        self.sal = sal

    def __str__(self):
        return f"age is: {self.age},gender is: {self.gender},name is: {self.name},salarry is: {self.sal}"

    def __getitem__(self, item):
        if item == 0:
            return self.age
        elif item == 1:
            return self.name
        elif item == 2:
            return self.sal
        else:
            raise IndexError("index out of range")

    def __len__(self):
        return len(self.__dict__)


a = int(input("enter your age "))
b = input("your gender")
c = input("enter your name ")
d = float(input("enter your salary "))
p = person(a, b, c, d)
print(p[0])
print(p[1])
print(p[2])
print("total instance member is: ", len(p))
