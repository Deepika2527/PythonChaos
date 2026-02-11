# int
import sys
age = 23
print(age)
print(type(age))
print('Memory allocation')
print(id(age))
print('Size....')
print(sys.getsizeof(age))

print('********')
age = 25
print(age)
print('Memory allocation')
print(id(age))

salary = 450000
print(salary)
print('Size....')
print(sys.getsizeof(salary))


# float 
pi = 31.4
print(pi)

print(type(pi))


# complex 
c = 4+5j
print(c)
print(type(c))
c1 = 3 -9j
print(c1)


#boolean- bool 

isRaining = False
print(isRaining)

if isRaining:
    print("Carry Umbrella")

print(type(isRaining))

islogged = 0
if(islogged):
    print('Welcome')

print(type(islogged))





