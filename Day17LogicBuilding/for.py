l = [1,2,3,4,5]
for i in l:
    print(i)


for j in range(1,11,2):
    print(j)

print("Nested Loops...")
l1 = [[1,2,3,4],[5,6,7,8]]
print(l1)
for j in l1:
    for k in j:
        print(k)
print("Using List comprehesions")
res = [b for a in l1 for b in a]
print(res)


# printstatement

print("Hello", end="-")
print("Hi....")


print("*" * 5)
print(" "+ "*")
print("-"*5+ "*"*7)
print(" "*5+ " * "*5)


# patterns
print("Pattern Right Triangle...")
for i in range(1,6):
    print('*'*i)
print("Inverted Right triangles")
for i in range(5,0,-1):
    print('*' * i)


print("Left Triangle..")
for i in range(1,6):
    print(" "*(5-i)+ '*'*i)
print("Inverted left Triangle...")
for i in range(5,0,-1):
    print(" "*(5-i)+ '*'*i)


