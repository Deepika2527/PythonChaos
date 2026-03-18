def val(a,b):
    print(f'Value of A is {a} and Value of B is {b} ')
val(10,2)

def student_details(name,course):
    print('Name : ', name)
    print('Course : ', course)
student_details("Abc",'Python')

def employee_det(id,name,role):
    print(f'The employee Id is {id}, and name is {name},role is {role}')
employee_det(101,'Nikath','FDeveloper')
employee_det('Tarannum', 101, 'BDeveloper')

def add(a,b,c):
    return a+b+c
res= add(10,20,30)
print(res)


def fruits(fruits):
    for f in fruits:
        print(f)
fruits(['Apple','Banana','Kiwi'])
# task
# def students(std):
#     for st in std:
#         print(st[0])
#         print(students[st])
# students(["Anu","Tara","Niki","Fathima"])

def billing(items,price):
    print("Items :", items)
    print("Prices :", price)
billing(['Milk','Curd'],(30,35))

def nos(a,b,c):
    print(a,b,c)

num = [1,2,3]
nos(*num)