class Dog:
    def __init__(self):
        self.name = "Bonkers"
        self.age = 4
    def bark(self):
        self.breed = "shihTzu"
        print(f"My Pet Name Is {self.name}- Age {self.age}- Breed {self.breed}")

d = Dog()
print(d.__dict__)
d.bark()


class Test:
    def __init__(name,nm,age):
        print("This is Constructor")
        name.name = nm
        name.age = age
    def m1(name):
        print("This is inside the m1()")
        print(f"Name is {name.name}")
        print(f"Age is {name.age}")
t = Test("abc",45)
t.m1()

print("Without constructor")

class Student:
    def interview(self):
        print(f"Student {self.name} has an interview on {self.role} role")
s = Student()
s.name = "Taranuum"
s.role = "Developer"
s.interview()
s1 = Student()
s.name = "Nikath"
s.role = "Tester"
s.interview()
s2 = Student()
s2.name = "Fathima"
s2.role = "Fullstack Developer"
s2.interview()