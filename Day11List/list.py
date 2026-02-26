l = [1,2,3,4,5,6]
print(l)
print(type(l))
print(id(l))
# mutable
l[0] = 10
print(l)
print(id(l))
# hetereogenous
listd = ["Hello",32.4,False,123,(12,34),[12,3,45],'World']
print(listd)
print(type(listd))
print(listd[4][1])
print(listd[5][2])

print(listd[2])
print(listd[6])
print(len(listd))
'''print(listd[7])-if the range is exceed it will show out of range'''


# creating list using list method
l = [1,2,3]
print(l)
l1= list([12])
print(l1)
l2 = list('python')
print(l2)
l3 = list(['hello','world'])
print(l3)
l4 = list(("django","python"))
print(l4)


# enumerate,range
lst = [1,2,3,5,7,8]
for n in range(len(lst)):
    print(n, lst[n])
    
# enumerate
for keys,values in enumerate(lst):
    print(keys,values)


ls1 = [1,2]
ls2 = [3,4]

print(ls1+ls2)
# print(ls1 * ls2)
print(ls1 * 3)


# membership
print(5 in [5,4])
print([5,4] in [5,4])
print([5,4] in [[5,4]])


a = [1,2,3,10,5,6,7]


print(a[1::1])
print(a[::1])
print(a[::2])
print(a[::-1])
print(a[-3:-1])
print(a[-1:-3])
print(a[4:1])
print(a[4:1:-1])
print(a[-1:-3:-1])


aa = [1,2,3,10,5,6,7]
aa[1:1] = [10]
print(aa)

print(aa)
aa[2:5] =[12]
print(aa)


