subject = {'math': 7,'english' : 9,'hindi':8}
print(subject)
print(subject.keys())
print(subject.values())
print(subject.items())
print("using setdefault.........")
print(subject.setdefault('hindi'))
print(subject.setdefault('science',5))
print(subject)
print("using get..........")
print(subject.get('math'))
print(subject.get('social',10))
print(subject)



data = ['a','b','c','d']
print(data)
res = dict.fromkeys(data,'undefined')
print(res)

data1 = {'a':'Hello', 'b':'All' , 'c':'Python' , 'd': 'students'}
print(data1)
print(data1.pop('b'))
print(data1)
print(data1.popitem())
print(data1)


data2 = data1.copy()
print(data2)

data2['c'] = "django"
print(data2)
print(data1)


data2.update({'mode':'online'})
print(data2)




