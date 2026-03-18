def demo(a,b,c):
    print("A value : ", a)
    print("B Value :" , b)
    print("C Value :",c)
demo(a=10,b=20,c=30)

def stud(n1,n2,n3):
    print("St1 :", n1)
    print("St2 :", n2)
    print("St3 :", n3)
stud(n1='Tara',n2='Nikki', n3 ="Fathima")
print("********************************")
stud(n3='Tara',n2='Nikki', n1 ="Fathima")


print("Postional and keyword argumenst are together")

def demo(a,b,x,y):
    print("A and B are: ", a,b)
    print("X and Y are :", x,y)
demo(10,20,x='a',y='b')
# demo(10,x="hello",y="bi")
# demo(x=10,y=10,11,23)



def only(i,j, /):
    print(i , "-", j)
# only(i="Hello" , j ="Python")
only("Hello" , "Python")

def onlyk(*,m,n):
    print(m,":", n)
onlyk(m=12,n=13)

def mix(a,b,/,*,c,d):
    print("A :", a)
    print("B :", b)
    print("C :", c)
    print("D :",d)
mix(10,20,c=30,d=40)


