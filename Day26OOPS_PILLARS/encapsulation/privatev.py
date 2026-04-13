class Student:
    def __init__(self,name,__marks):
        self.name = name
        self.__marks = __marks
    def disp_marks(self):
        print("Name: ", self.name)
        print("Marks: ", self.__marks)
s = Student("Std1",100)
s.disp_marks()
print(s.name)
# print(s.__marks)
# print(s.Student__marks)
print("__________________")
print(s._Student__marks)  
print("__________________")




class Student:
    def __init__(self,__marks):
        self.__marks = __marks
    def disp(self):
        print(f"Inital marks {self.__marks}")
    def get_marks(self):
        return self.__marks
    def set_marks(self,v):
       
        if 0<= v <=100:
            self.__marks = v
        else:
            print("invalid marks❌")
s = Student(100)
s.disp()
print(s.get_marks())
s.set_marks(90)
print(s.get_marks())


