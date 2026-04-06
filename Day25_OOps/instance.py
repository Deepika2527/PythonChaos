class Demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.role = "Developer"
    def m1(self):
        self.company = "Abc"
        print(f"Hello, {self.name}-{self.age}-{self.role}")
        print(f"Hello, {self.name}-{self.age}-{self.role}-{self.company}")
        del self.company
        # print(f"Hello, {self.name}-{self.age}-{self.role}-{self.company}")
d = Demo("Fathima",20)
d.m1()
print(d.__dict__)
d2 =Demo("Nikath",20)
d2.m1()
print("Creating Intance varaible outside of the object of the creation")
d2.place = "Hyd"
print(d2.__dict__)
d2.place = "CHENNAI"
print(d2.__dict__)
print(Demo.__dict__)