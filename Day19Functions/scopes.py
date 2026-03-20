print("Global scope")

a = 10
def test():
    print("Helllo....")
    print(a)
    print("BI.................")
test()
print(a)

for i in range(1,5):
    print(i)
    print(a)


# ex3
institute_name = "Ait"

def students():
    print(f'Hello students, Welcome to {institute_name}')
students()

cart = ["jeans","kurthi","salwar","dupatta"]

def billing(total):
    print(f'I have Shopped {cart} and total is {total}')
billing(3000)


print("_________________________________________")
def test():
    enrolled = True
    print(f"Can add into the batch {enrolled}")
test()
# print(enrolled)


clz_name = "Pragnya Clz"
def stds():
    library = ['staff','students']
    print(f"Welcome to {clz_name}. Only {library} can access the Library")
stds()


def with_drawl():
    amount = 1000
    deposit = 1000
    deposit += amount
    print(deposit)
with_drawl()


print("__________________________________")
a = 10
def mix():
    print(a)
    b = 20
    print(b)
mix()
print(a)


course = "react"
def crs():
    course = "python"
    print("Inside fun", course)
    print(id(course))
crs()
print("Outside function", course)
print(id(course))

x = 100
def both():
    global x
    x = 200
    print("Using global ", x)
both()
print("After the function " ,x)

'''z ="hello"
def testng():
    z= "Hello"
    global z
    print(z)
testng()
'''

z ="hello"
def testng():
    global z
    z= "Hello"
    
    print(z)
testng()



count = 0
def counter():
    global count
    count = count+1
    print("The count value is : ", count)
counter()
counter()
counter()


balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print("Deposited amount : ", balance)

def with_drawl(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawl: ", amount , "Balance : ", balance)
    else:
        print("Insufficient balance")

deposit(2000)  #3000
deposit(5000)
with_drawl(1000)
with_drawl(8000)

