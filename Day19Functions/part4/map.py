# def square(x):
#     return x*x
# nums = [1,2,3,5]
# result = map(square, nums )
# print(result)
# print(list(result))

# print("Using lambda function------------------------------")
# res = tuple(map(lambda x : x*x,nums))
# print(res)

# res1 = list(map(lambda p : p*0.9,[1000,2000]))
# print(res1)

names = ["tarannum","sara","fathima","nikath","bonkers","bonky"]

# res2 = list(map(lambda st: [s if s.startswith("b") else "not starts with b" for s in st],names))
# print(res2)
res3 = list(map(str.upper,names))
print(res3)

n = ['1','45','34','89']
res4 = list(map(int,n))
print(res4)

