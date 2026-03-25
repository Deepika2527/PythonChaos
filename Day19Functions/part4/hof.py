# def test(function):
#     print("Hello this is testing function...")
# test("hllo")
# def demo():
#     print("Hello this id demo function")
# demo()


def test(function):
    print("Hello this is testing function...")
    function()

def demo():
    print("Hello this is demo function")
test(demo)

print("-----------------------------------")
def greeting(fun):
    print("This is greeting function")
    fun()
def morning():
    print("Hello Good Morning........")
def evening():
    print("Hello Good Evening.........")
greeting(morning)
greeting(evening)

print("----------------------------")

def operations(fn,a,b):
    print("This is operation functionssss..")
    return fn(a,b)
def add(m,n):
    return m+n
def mul(m,n):
    return m*n
print(operations(add,10,20))
print(operations(mul,10,20))

print("Case 2: using return statement in hof")
def outer():
    print("This is Outer function")
    def inner():
        print("This is inner function")
    return inner
res = outer()
print(res)
res()



def greet(time):
    def morning():
        return "Good Morning"
       
    def evening():
         return "Good Evening"
    if time == "morning":
        return morning
    else:
        return evening
func = greet("morning")
print(func())

print("with closure")
def power(n):
    def inner(x):
        return x ** n
    return inner
square = power(2)
cube = power(3)
print(square(5))
print(cube(5))