def outer():
    x = "hi"
    def inner():
        print(x)
    inner()
outer()

'''def nouter():
    name = "python"
    def ninner():
        name = "Python"
        print("Inside of the inner : ", name)
    ninner()
    print("After the inner function : ",name)
nouter()'''
# print("Outsise od the function", name)


def nouter():
    name = "python"
    def ninner():
        nonlocal name
        name = "Python"
        print("Inside of the inner : ", name)
    ninner()
    print("After the inner function : ",name)
nouter()


print("Differnce btween global and nonlocal")

n = "python"
def gouter():
    n = "react"
    def ginner():
        global n
        n = "django"
        print("Inisde Inner :", n)
    ginner()
    print("Outside inner :", n)
gouter()
print("Oustide of the function :", n)

print("With nonlocal------------------------")
m = "python"
def nlouter():
    m = "react"
    def nlinner():
        nonlocal m
        m = "django"
        print("Inisde Inner :", m)
    nlinner()
    print("Outside inner :", m)
nlouter()
print("Oustide of the function :", m)


print("legb")

def demo():
    a = 10  #local
    print(a)
demo()

def demo1():
    a1 = 100
    def inner():
        print(a1)
    inner()
demo1()

a2 = 30
def demo3():
    print(a2)
demo3()
print("hello.............")



s = 23
def test():
    s = 30
    def innertest():
        s= 45
        print(s)
    innertest()
    print(s)
test()
print(s)