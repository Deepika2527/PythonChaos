'''

while loop -This will executes as long as the condtion is True



syntax: 
initalisation
while(condtion):
    statement
    inc








'''

i = 1
while(i<=5):
    print(i)
    i+=1

print("Using the range.....")
for i in range(10):
    if i == 5:
        break
    print(i)
for j in range(2,7):
    if j ==3:
        continue
    print(j)
 
for a in range(5):
    for j in range(4):
        print(a, j)
'''
a 0 1 2
j 0 1



'''