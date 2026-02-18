# units = int(input("Enter the units : "))

# if(units>=300):
#     print("Bill is 3000")
# elif(units>=200):
#     print('Bill is 2000')
# elif(units >=100):
#     print('Bill is 1000')
# else:
#     print('Currennt is free')


# example 2
# course =  input('Enter the course: ')
# if(course == 'python'):
#     print('ends with .py extenstion')
# elif(course == 'js'):
#     print('Ends with .js extenstion')
# elif(course == 'html'):
#     print("Ends with .html extenstion")
# elif(course == 'css'):
#     print("Ends with .css")
# else:
#     print("Invalid input")

# 
day = input("Enter the day : ")
if(day in ['mon','tue']):
    print('Need to go to the office complete 8 hours..😒')
elif(day in ['wed','thur']):
    print("Need to go to the office for 5 hours..")
elif(day in ['fri']):
    print("Work from Home")
else:
    print("Hurray its sat and sunday..😎")