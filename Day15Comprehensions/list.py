n = [1,2,3,4,5,6]
l= []
for i in n:
    l.append(i*i)
print(l)
print("Using list comprehensions")
# [expression for item in iterable]
res= [ns*ns for ns in n]
print(res)

# to print the range

ranze = [l+2 for l in range(1,5)]
print(ranze)


# numbers to stings

no = [1,2,4,7,100]
no_sting = [str(j) for j in no]
print(no_sting)


# uppercase

chars = ['a','b','c','d']
to_uppercase =  [c.upper() for c in chars]
print(to_uppercase)


# lenght of each word
words = ["Words","Knowledge","Success","test"]
lengh_word = [len(w) for w in words]
print(lengh_word)



# [expression if item in iterable if_condition]
print("List comprehensions using if condtion")

num =  [12,4,52,3,4,6,71,90,31,56,77,11]
even_n = [even for even in num if even%2==0]
print(even_n)
print(num)

odd_n = [odd for odd in num if odd%2!=0]
print(odd_n)


print("Numbers that are greater than 5")

l = [1,5,6,90,0,-1,56,10]
resl = [res for res in l if res>5]
print(resl)

print("Multiplication of 3")

mult =  [i for i in range(1,22) if i%3 ==0]
print(mult)



print("Using if else.........")
lst = [1,2,43,3,6,9,21,90]
result = ['Even' if n%2==0 else 'Odd' for n in lst]
print(result)

print("Using range")

even_odd = ['Even' if i%2==0 else 'Odd' for i in range(1,11)]
print(even_odd)



sent = "knowledge"

reslt =  [res if res in 'aeiou' else '-' for res in sent]
print(reslt)



print("Replacenegative with 0")
n = [12,-3,5,7,-2,-1]
rplce = [0 if m<0 else m for m in n]
print(rplce)



print("List comprehension")

matrix =  [[1,2,3,],[4,5,6],[7,8,9]]
result = [num for row in matrix for num in row ]
print(result)


print("Covert the nesetd list to Uppercae")
words = [['apple'],['banana'],['kiwi']]

res = [word.upper() for row in words for word in row]
print(res)