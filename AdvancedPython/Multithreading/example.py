from threading import *
from time import *





# def num():
#     for i in range(1,10):
#         print(i)
# t = Thread(target=num)
# t.start()
# t.join()
# print("Main program.....")


# print("Without join")

# def numb():
#     for i in range(4):
#         print("Child Thread: ", i)
# t = Thread(target=numb)
# print("Before start")
# t.start()
# print("After start")
# print("Main code")




# print("Without join")

# def numb():
#     for i in range(4):
#         print("Child Thread: ", i)
# t = Thread(target=numb)
# print("Before start")
# t.start()
# t.join()
# print("After start")
# print("Main code")



# print("Is Thread Alive :", current_thread().is_alive())
# def sum(a,b,c,d):
#     print("Current Thread :", current_thread().name)
#     print("Is Thread Alive :", current_thread().is_alive())
#     print("Identification number", current_thread().ident)
#     print("is Daemon Thread:", current_thread().daemon)
    
#     print("Args :", a,b)
#     print("kwargs :", c,d)
#     print("Total Thread:", a+b+c+d)
# t = Thread(target=sum,name="addition",args=(100,20),kwargs={'c':10,'d':50},daemon=True)
# t.start()
# t.join()
# print("Hello")
# # print("Is Thread Alive :", current_thread().is_alive())




# def numbers():
#     for i in range(65,91):
#         print("Numbers :", i)
#         sleep(3)
# def aplha():
#     for j in range(65,91):
#         print(chr(j))
#         sleep(7)
# t = Thread(target =numbers)
# t1 = Thread(target = aplha)

# t.start()
# t1.start()

# t.join()
# t1.join()




# def test():
#     print("-------Thread started-----")
#     sleep(0.5)
#     print("------------Thread ended--------")
# t = Thread(target = test)
# print("****************Main Program starts*****************")
# t.start()
# sleep(1)
# print("********************Main programm ends*******************")

# print("_______________________________________")
# def demo():
#     print("Child Thread started🌟" )
#     sleep(1)
#     print("It will never executes ❌❌")
# t = Thread(target=demo,daemon=True)
# print("Main progrem started😎")
# t.start()
# sleep(0.5)
# print("Main Prgram ends...💥❤️")




# print("Racing condtion")

# def display(str):
#     for s in str:
#         print(s)
#         sleep(0.5)
    
# t = Thread(target=display,args=("Hello",))
# t1 = Thread(target=display,args=("Python",))

# t.start()
# t1.start()




print("--------semaphore---------")

def display(str):
    l.acquire()
    for s in str:
        print(s)
        sleep(0.5)
    l.release()
    
t = Thread(target=display,args=("Hello",))
t1 = Thread(target=display,args=("Python",))
t2 = Thread(target=display,args=("Testing",))

l = Semaphore(2)

t.start()
t1.start()
t2.start()


















# def number():
#     for i in range(1,10):
#         print(i)
# number()
# print("Starting....................")
# def ascii_val():
#     for j in range(65,91):
#         print(chr(j))

# ascii_val()
# print("Ending.........")