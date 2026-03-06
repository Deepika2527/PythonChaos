t = (10,2,3,[12,9],None)
print(t)
print(type(t))
print(t[0])
# t[0] = 100
# print(t)
t[3][1] = 90
print(t)



t1 = 10,20,30
print(t1)
print(type(t1))


# using constructor
t2 = tuple([12,4])
print(t2)
print(type(t2))


t3 = ((12,))
print(t3)
print(type(t3))
t4 = ((14))
print(t4)
print(type(t4))


t6 = (10,20,30,40,50,10,30,30)
print(t6.count(30))
print(t6.count(100))
print(t6.index(20))