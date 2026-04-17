import re


# str1 = re.match("Hello","Hello all")
# print(str1)
# str2 = re.match("Hello","all Hello")z
# print(str2)
# str3 = re.match("hello","python")
# print(str3)


# print("------------------------------------------------")

# print("Search method")
# s = re.search("Hello","Hello world")
# print(s)
# s1 = re.search("Hello","Hi -Im from python i want to say Hello")
# print(s1)
# s2 = re.search("python","django")
# print(s2)


# print("------------------------------------------------")

# replace = re.sub("python","django","I love python")
# print(replace)


# s1 = re.search("hello ","hello all").span()
# print(s1)
# s2 = re.search("hello_a", "hello_all").group()
# print(s2)



print("----------------------------------------------------------")
# s = re.findall("Hello", "Hello all Hello hi")
# print(s)
# s1 = re.findall("a","banana")
# print(s1)
# s2 = re.findall("123","the code is 123")
# print(s2)
# s3 = re.findall("123","456")
# print(s3)


s4 = re.finditer("aa","bananaa")
print(s4)
for res in s4:
    print(res.span(), res.group())




# print("-------------Quantifiers------------------------------------")
# t = re.findall("a","banana")
# print(t)
# t = re.findall("a*","banananaaa na aaa a naa")
# print(t)
# t1= re.findall("a+","banana")
# print(t1)
# t2 = re.findall("a+","ba baaa baaa baaaaa ba tt")
# print(t2)
# t3 = re.findall("colou?r","colour color")
# print(t3)
# t4 = re.findall("colo?ur","colour color")
# print(t4)
# t5 = re.findall("a{2,5}","bananaa aaa bbb aabaa aaaaaaa aaaaa")
# print(t5)

# t6 = re.findall("a{3,}","cat aa is aaaangry")
# print(t6)
# t7 = re.findall("t{,2}", "tempting offers in the dmartt")
# print(t7)


print("---------------------------------------------------")
d = re.findall("[0-9]","welcome@128906543")
print(d)
d1 = re.findall("\d","1234")
print(d1)
d2 = re.findall("^\d","1234")
print(d2)
d3 = re.findall("^\d+$","123")
print(d3)
print("Regex Part2")
d4 = re.findall("[^a-z]","printmeAbBDJHLDKJSHJD")
print(d4)
d5 = re.findall("\w","%*Hello all 123")
print(d5)
d6 = re.findall("\W","%*Hello all 123")
print(d6)
d7 = re.findall("^\W","--")
print(d7)

print("-----------------------------------------------------------")

print(re.findall(".a","bat cat flat trap tt 9a at"))


print("Grredy and non greedy")
print(re.findall('a','aaaaaaa'))
print(re.findall('a+','aaaaaaa'))
print(re.findall('a+?','aaaaaaa'))
text = "<h1>Hello</h1><span>"

print(re.findall("<.*>",text))
print(re.findall("<.*?>",text))



text = "hello Hello HI"
res = re.findall("hello",text,re.IGNORECASE)
print(res)
res1 = re.findall("(?i)hello", text)
print(res1)
