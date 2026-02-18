#  Identity-is, is  not
''' Identity is used for memoryallocation'''


a = 10
b = a
c = 20

print(id(a))
print(id(b))
print(a is b)
print(a == b)
print('Using is not')
print(a is not b)

l = [12,34]
l1 =  [12,34]
print(id(l))
print(id(l1))
print(l is l1)
print(l == l1)


st = "Python"
st1 = "Python"
print(st is st1)

a = 100
b = 100
print(a is b)


s = {1,2,4}
s1 = {1,2,4}
print(s is s1)

print( s == s1)



person = {
    'name' : 'Fathima',
    'class' : 'python'
}

person1 = {
'name' : 'Fathima',
    'class' : 'python'
}
print('name' is person)
print(id(person))
print(id(person1))
print(person is person1)
print( person == person1)

