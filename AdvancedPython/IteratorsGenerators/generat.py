def w_retunr():
    return 10
    # return 200
a = w_retunr()
print(a)


def demo():
    yield 1
    yield 2
g = demo()
print(next(g))
print(next(g))
print("---------------------------------")
def test():
    print("Hello im the starting")
    yield 1
    print("Im the middel")
    yield 2
    print("Ending")
    yield 3

t = test()
print(next(t))
print(next(t))
print(next(t))


def even():
    for i in range(10):
        if i%2 == 0:
            yield i
e = even()
for a in e:
    print(a)


print("using expression")
g = (i*i for i in range(20))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = (i+1 for i in range(200))
res = list(g)
# print(res)
it = iter(res)
print(next(it))