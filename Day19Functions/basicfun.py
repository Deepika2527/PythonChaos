print("Definig the function...............")


'''def greet():
    print("Hello all")
greet()
greet()'''

'''print("When the function returns nothing, then we get None as output")
def test():
    print("Welcome to python class")

res = test()
res
print(res)
'''

print("Using return")

def display():
    print("Im test function using return")
    return "exectued successfully..."
result = display()
result
print(result)



print("Calling the function before")

# maths()
def maths():
    print(5+8)
# maths()

def operations(a,b):
    print('Addtion', a+b)
    print('Subratction', a-b)
    print('Mul', a*b)

operations(10,2)

def maths(x,y):
    return x+y, x-y, x*y, x/y, x//y
# res = maths(10,2)
# print(res)
# print(type(res)) #this will return tuple
# for r in res:
#     print(r)

# (x,y) =maths(12,3)
# print(x)
# print(y)
