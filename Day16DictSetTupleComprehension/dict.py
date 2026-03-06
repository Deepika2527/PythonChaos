n = [1,2,3,4,5,6,7]

newdic =  {i:i+1 for i in n}
print(newdic)

squ = {s:s*s for s in n}
print(squ)
print(type(squ))

cube = {c: c**3 for c in n}
print(cube)


word =  ['Tarannum','Nikath','Fathima']
leng =  {l:len(l) for l in word}
print(leng)


'''l
taranumm - t.... : 8
Nikath - N.... :6
Fathima - Fa...:7



'''

print('dict com with range..')
rng = {r:r-1 for r in range(1,10)}
print(rng)

print("Dict with if condtions")

no = [1,2,3,4,5,6,7,8,9,10]

even =  {e:e+2 for e in no if e%2==0}
print(even)


words = ["Lion","Tiger","Elephant","Cat","Doggy"]

len1 = {l:len(l) for l in words if len(l)>3}
print(len1)


d = {x:x*3 for x in range(1,11) if x%3==0}
print(d)

nums = [-3,-2,10,-4,9,10]
d1 = {i:i**2 for i in nums if i>0}
print(d1)

names = ["Hari",'geetha',"Maggie","maxy"]
d2= {j:len(j) for j in names if len(j)==4}
print(d2)


print("Dict comprehension using if-else")
n =[12,45,11,56,75,23,35,28]
res = {i:"Even" if i%2==0 else 'odd' for i in n}
print(res)

num = [12,4,-5,9,-3]
res = {j:'Positive' if j>0 else 'Negative' for j in num}
print(res)

word = ["Pen","Notebook","textbook","scale"]
d = {w:"Long" if len(w)>4 else "Short" for w in word}
print(d)




print("Tuple comprehension.....")
l = [1,2,4,5]
t = (i for i in l)
print(t)
print(type(t))
print(next(t))
print("How we need to use exactly")
t1 = tuple(j for j in l)
print(t1)
print(type(t1))
t2= tuple(k for k in l if k>2)
print(t2)
t3 = tuple('Even' if j%2==0 else 'Odd' for j in l)
print(t3)


# setcomprhension
print('Set comprehension...')

s = {i for i in range(1,10,2)}
print(s)
print(type(s))

s1 = {j for j in range(2,50) if j>5}
print(s1)
s2 = {k for k in range(1,51) if k%5==0}
print(s2)


word = "pytJon"
s3 = {w.upper() if w.islower() else w.title() for w in word}
print(s3)
