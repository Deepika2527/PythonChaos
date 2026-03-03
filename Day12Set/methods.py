s = {1,2,4}
# print(s.add(12))
# print(s)
'''print(s.add(13,4))
print(s)
Add method will take only one arguments


'''
# print(s.add('hi'))
# print(s)
'''print("Adding dic")
print(s.add({"1":3}))
print(s)'''
'''print(s.add([1,23]))
print(s)'''

# print(s.add((120,)))
# print(s)



print('update')
print(s)
s.update((1123,145))
print(s)
print(s.update(((100,200),)))
print("****")
print(s)
print(s.update([1000,"klo"]))
print(s)



a = {1,2,4}
b = {3,5,7}
print(a.pop())
print(a)


print(a.clear())
print(a)

'''del(a)
print(a)
'''
print(b.remove(3))
print(b)







print("remove vs discard")
c = {1,2,4,5,6,7,8}
# c.remove(2)
# print(c)
# c.remove(20)
# print(c)

c.discard(5)
print(c)
c.discard(50)
print(c)

