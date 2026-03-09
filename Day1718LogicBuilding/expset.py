# sum of the values
'''count = 0
n = int(input('Enter the Number: '))
for i in range(1,n):
    count += i
print(count)



print("Reverse")

st = input("Enter the string: ")
rev = ""
for ch in st:
    rev = ch+rev
    print(rev)

'''

print("Removing Duplicates")
l = [1,2,3,4,5,1,3,5]
seen = []
dup = []

for i in l:
    if i not in seen:
        seen.append(i)
    else:
        dup.append(i)
print(dup)