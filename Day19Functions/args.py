def num(*args):
    print(args)
num(12,3,4,5)


def no(*ar):
    print(len(ar))
    for n in ar:
        print(n)
no([12,3,4,5,6,6],None)


print('----------------------------------')

def add(*no):
    total = 0
    for n in no:
        total += n
    print(total)
add(12,3,4,10,11)

def add(*n):
    print(sum(n))
add(10,20,30)

print("postional argument and then args")

def birthday(name,*args):
    print(f'Hello all, Lets sing "Happy Birthday song to...."{name}, she is {args} old')
birthday('Tarannum', 16,17)


def numbers(a,*args,b):
    print("Postional :", a)
    print("Args : ", args)
    print("Keywords : ",b)
# numbers(10,12,34,56,78)
numbers(10,12,34,56,78,b=100)