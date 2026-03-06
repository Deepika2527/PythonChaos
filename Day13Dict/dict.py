dic = {
    'name' : "Python",
    "students" : 3,
    "mode" :'online',
    "mode" : 'offline'
}
print(dic)
print(type(dic))

# access the values
print(dic['name'])
'''print(dic[0]) -keyError'''


d = {}
print(type(d))

s = set()
print(type(s))


# ways to create dict
# w1- using list

d1 = dict([(1,2),(3,4),(5,6)])
print(d1)
print(type(d1))

# way to using tuple

d2 =  dict((('name','Alice'),('age',25),('role','developer')))
print(d2)

#3rd way is keyword argunet
print("Using keyword argument")
stdn =  dict(name ="Deepika", course = "python" , cls = "online")
print(stdn)
stdn['name'] = "Fathima"
print(stdn)






student = {
    'name' : 'Bob',
    'age'  :20,
    'percentage' : 90.9,
    'complex' : 24+5j,
    'ispassed' : True,
    'course' : ['Html','css'],
    'versions' :('html5','css3'),
    'duration' :{1,2},
    'phoneNo' :{'firstNo':909090,'adress' : 'hyd'}



}
print(student)
print(student['phoneNo'])
print(student['duration'])
print(student['versions'])
print(student['course'][1])
print(student['phoneNo']['firstNo'])
print(student['versions'][0])


# 

std = {

    'name' : 'mark',
    24 : 'age',
    67.9 : 'percentage',
    45+7j : 'complex',
    ('html','css') : 'Frotnend',
    # {1:3} : 'dict',
    # {2,4} : 'postive numbers'
    # ['Python','django'] : 'backend',
}
print(std)




