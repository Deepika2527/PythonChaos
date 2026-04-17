from multiprocessing import *

# def order_place(q):
#     orders = ["Pizza","Burger","chips"]
#     for order in orders:
#         print("Placed:", order)
#         q.put(order)
# def receive_order(q):
#     while not q.empty():
#         print("Served:", q.get())
# if __name__ == "__main__":
#     q = Queue()

#     p1 = Process(target=order_place,args=(q,))
#     p2 = Process(target=receive_order,args=(q,))

#     p1.start()
#     p2.start()


#     p1.join()
#     p2.join()


# print("using pipes")
# def user1(conn):
#     conn.send("Hi user2✋")
#     print("User1 sent meassge")
#     conn.close()
# def user2(conn):
#     mgs = conn.recv()
#     print("User2 recived:", mgs)
#     conn.close()
# if __name__ == "__main__":
#     conn1,conn2 =Pipe()

#     p1 = Process(target=user1,args=(conn1,))
#     p2 = Process(target=user2,args=(conn2,))


#     p1.start()
#     p2.start()


#     p1.join()
#     p2.join()


print("using shared memory....")
def update(num):
    num.value += 10

if __name__ == "__main__":
    num = Value("i",10)


    p = Process(target= update, args=(num,))
    p.start()
    p.join()
    print(num.value)

