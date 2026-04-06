# class Demo:
#     x = 10
#     def __init__(self):
#         self.y = 20
#     def m1(self):
#         print(self.y)
#         # print(Demo.y)
# t1 = Demo()
# t2 = Demo()
# t3 =Demo()
# print("T1: ", t1.x, t1.y)
# print("T2: ", t2.x, t2.y)
# print("T3: ", t3.x, t3.y)
# t2.y = 200
# Demo.x = 100
# print("After changing the values....  ")
# print("T1: ", t1.x, t1.y)
# print("T2: ", t2.x, t2.y)
# print("T3: ", t3.x, t3.y)

# print(t1.__dict__)
# print(Demo.__dict__)

# t1.x = 1000
# print(t1.__dict__)
# print(Demo.__dict__)


class Test:
    a = 20
    def __init__(self):
        self.b = 30
    # def m1(self):
    #     print("Creating  class varaible inside the instance method using className.varaiblename")
    #     Test.c = 40
    #     print(Test.c)
    #     print(self.b)
    # @staticmethod
    # def m2():
    #     Test.d = 50
    #     print(Test.d)
    #     Test.d = 500
    #     print(Test.d)
    @classmethod
    def m3(cls):
        cls.e = 60
        print(cls.e)




# t = Test()
# t.m1()
# print(Test.__dict__)
# print(t.__dict__)

t1=  Test()
# t1.m2()
# # Test.d = 500
# t1.m2()

t1.m3()
Test.f = 70
print(Test.__dict__)