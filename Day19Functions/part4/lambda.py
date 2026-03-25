def add(a,b):
    return a+b
res = add(10,20)
print(res)

print("Using lambda functions------------------------------")
res = lambda x,y: x+y
print(res(1,3))
res1 = lambda n: n*n
print(res1(10))
print("Even or odd")
res2 = lambda no : "Yes-even" if no%2 == 0 else "No-odd"
print(res2(10))
print(res2(11))


res_3 = lambda st : st.lower()
print(res_3("DjaNGo"))

dic = {
    "a" : 10,
    "b" : 20,
    "c" :30

}
res_4 = lambda d : d['a']
print(res_4(dic))

res_5 = lambda d : sum(d.values())
print(res_5(dic))

res_6 = lambda l : sum(l)
print(res_6([1,2,3,4,5]))


cart = [1000,4000,5000,3000]
res_7 = lambda c : [i for i in c if i>1200]
print(res_7(cart))

marks = [35,78,99,56,34,56]
res_8 = lambda m : [i if i>=35 else "fail"  for i in m]
print(res_8(marks))

ages = [15,78,23,56,18]
res_9 = lambda age: ["major"  if ag >=18 else "minor" for ag in age]
print(res_9(ages))
