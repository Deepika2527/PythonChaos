a = [1,2,3,4,6,7]
print(a[0])
print(a[1])

for i in range(10):
    print(i)


print("using iteratos")
a = [123,678,9,00,78]
it = iter(a)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print("----------------------")
s = {67,8,9,0,1}
itr = iter(s)
print(next(itr))
print(next(itr))
print(next(itr))
print("-----------------------")
t = (23,5,6,8)
tup = iter(t)
print(next(tup))
print(next(tup))
print(next(tup))
print(next(tup))
print("-----------------------------")

d = {"a":1,"b":2,"c":3}
dic = iter(d)
print(next(dic))
print("dict with value")
dic_v = iter(d.values())
print(next(dic_v))
print("Key-values")
dictn = iter(d.items())
print(next(dictn))

print("suing functions...")
def count(data):
    d = iter(data)
    print(next(d))
    print(next(d))
    print(next(d))
count(["Nikath","Fathima","Tarannum"])

def demo(lst):
    return iter(lst)
d = demo({"Apple","Html","Python"})
# print(next(d))
# print(next(d))
# print(next(d))

for i in d:
    print(i)
print("---------------------------")
def exmp(t):
    it = iter(t)
    while True:
        try:
            print(next(it))
            print(next(it))
        except StopIteration:
            break
exmp((12,56,789))


class Count:
    def __init__(self):
        self.value = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.value <= 6:
            res = self.value
            self.value += 1
            return res
        else:
            raise StopIteration

    
c = Count()
print(c)
for i in c:
    print(i)
print("---------------------------------")
class Mylist:
    def __init__(self):
        self.data = [12,3,4,6,7]
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index+=1
            return val
        else:
            raise StopIteration
        
    
m = Mylist()
for res in m:
    print(res)

print("----------------------------")
for i in range(1000):
    print(i)
n = iter(range(100))
print(next(n))
