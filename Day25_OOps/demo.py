class Car:
    def __init__(self,name,color,fuelT):
        self.name = name
        self.color = color
        self.fuelT = fuelT
    def start(self):
        print(f"Th car name is {self.name} and the color is {self.color}")
    def stop(self):
        print(f"The car ran out of fuel need to refill the fuel,so fuel Type is {self.fuelT}")
c = Car("Punch","Black","Petrol")
# c.start()
# c.stop()
# print(c.name)
# print(c.color)
print("This is a dummy lin e.....")
# ?creating one more object
print("Creati ng one more object")
c1 = Car("Toyato","white","Disel")
c1.stop()

def student(n,a):
    print("Name :", n)
    print("Age : ", a)
student("Test",10)
student("Test2",12)

print(c.name)
# print(student.name)

print(c.color)
        


class Student:
    def __init__(self,name,id,course):
        self.name = name
        self.id = id
        self.course = course
    def interview(self):
        print(f"The studnet {self.name} with an Id{self.id} did cousre {self.course} has craceked the interview")
    def job(self):
          print(f"The studnet {self.name} with an Id{self.id} did cousre {self.course} has craceked the interview")
s1 = Student("S1",101,"PFs")
s1.job()


class Bus:
    def __init__(self):
        self.name = "Redbus"
        self.fuelt = "petrol"

    def start(self,driver):
        print(driver)
        
        print("The bus name is", self.name)
# b= Bus()
# b.start("Xyz")
# print(b.name)

# print(b.fuelt)

Bus().start("John")
print(Bus().name)