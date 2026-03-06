students =  {'s1' : 'Bob' , 's2' : 'Max' , 's3' : 'Jack'}
print(students)
print(len(students))

print("Using for")
for s in students:
    print(s)
print("unsing enumerate")
for k,v in enumerate(students):
    print(k,v)
print("using items")
i= 0
for keys,values in students.items():
    print(i, keys,values)
    i+=1

print("Using enumerate and items")
for i,(k,v) in enumerate(students.items()):
    print(i,k,v)
