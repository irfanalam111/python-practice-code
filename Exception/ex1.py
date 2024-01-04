import dataclasses
class student:
    def __init__(self,name,roll,id):
        self.name=name
        self.roll=roll
        self.id=id
    def __str__(self):
        return f"name of student is : {self.name},roll number of student is : {self.roll},id of student id : {self.id}"
    
class program(student):
    def __init__(self,name,roll,id,stream="python,java"):
        self.name=name
        self.roll=roll
        self.id=id
        self.stream=stream
        super().__init__(name,roll,id)
    def __str__(self):
        return f"stream of student : {self.stream}"
        super().__str__()
a=input("enter student name : ")
b=input("enter roll number : ")
c=input("enter id : ")
d=program(a,b,c)
print(d)

