class person:
    def __init__(self, age, name, id, stream):
        self.age = age
        self.name = name
        self.id = id
        self.stream = stream

    def __str__(self):
        print(f"age{self.age},name{self.name}id{self.id}stream{self.stream}")


a = int(input("enter your age "))
b = input("enter your name")
c = int(input("enter your id"))
d = input("enter your stream")
obj = person(a, b, c, d)
print(obj)
