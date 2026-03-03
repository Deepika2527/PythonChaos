A = {1,2,3,4,5,6,7,8,9,10}
a = {1,2,3,4,5}
b = {5,6,7,8,9,10}
B = {1,2,3,4,5,6,7,8,9,10}

print(A.issuperset(B))
print(B.issuperset(A))

print("subset")
print(a.issubset(A))
print(A.issubset(a))

print(a.issubset(B))
print(b.issubset(B))

# ,
a= {1,2,3,4,5,6}
b = {5,7,8,9,0,6}
print("********")
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(a)
print(b)

print("with symbols")
print(a|b)
print(a&b)
print(a -b)
print(a ^ b)



a = {1,2,4,5}
b = {3,4,5,6,7}
print(a.intersection_update(b))
print(a)
print(b)