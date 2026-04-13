# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print(f"{self.name} got {self.marks} marks")
# s = Student("Std1",99)
# s.display()
# print("Accessing the marks", s.marks)
# s.marks = 50
# print("Accessing the marks", s.marks)
# s.marks = -100
# print("Accessing the marks", s.marks)


class Student:
    def __init__(self,name,_marks):
        self.name = name
        self._marks = _marks
    def display(self):
        print(f"{self.name} got {self._marks} marks")
s = Student("Std1",60)
s.display()
s._marks = 100
print("Updated marks", s._marks)


class Student:
    def __init__(self,_marks):
        self._marks = _marks
    def disp_show(self):
        print(f"Initiall marks {self._marks}")
class Child(Student):
    def marks(self,value):
        self.value = value
        self._marks = value
        print("Updated Marks are: ", self._marks)
m = Child(50)
m.disp_show()
m.marks(90)


