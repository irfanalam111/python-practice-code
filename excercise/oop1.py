class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" name is: {self.name},age is: {self.age}"


class student(person):
    def __init__(self, name, age, roll, grade):
        self.roll = roll
        self.grade = grade
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()},roll is: {self.roll},grade is: {self.grade}"


class teacher(person):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()},salary is: {self.salary}"


print(person('ram',25))
print(student('ram',25,49,'A'))