fruits = ["Apple","Mango","Kiwi"]
print(fruits)
fruits.append('Grapes')
'''fruits.append('strawberry','chiku')- one arguments'''
print(fruits)

# extends
l1 = [10,20,30]
# l1.extend([1,2,3])
l1.extend([(23.6),{'nm':'evening'}])
# [4,5,6].extend(l1)
print(l1)

'''Task- EWhy [4,5,6].extend(l1)
print(l1)
'''


# insert
lst = [1,2,4,5]
lst.insert(1,[12,{12,34}])
print(lst)
lst.pop()
print(lst)
lst.pop(2)
print(lst)

newli = [True,False,True,False,True,False]
print(newli)
newli.remove(True)
print(newli)
newli.clear()
print(newli)
'''del(newli)
print(newli)'''




a = [1,2,6,8,10,2,89]
a.sort()
print(a)
b= [12,10,34,10,34,100,0]
b.sort(reverse=True)
print(b)

c = ["Hello","world","of","Python"]
c.reverse()
print(c)



d= [1,2]
e = d.copy()
print(d)
print(e)
d[0]=10
print(d)
print(e)
print(id(d))
print(id(e))