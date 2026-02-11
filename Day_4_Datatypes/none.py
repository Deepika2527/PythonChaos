x = None
print(x)
print(type(x))


def greet():
    print('hello')
    # return 'Bye..im going...'

disp = greet()
print(disp)


person = {
    'name' : 'xyz',
    'course' : None
}

print(person)


# byte -bytearray

byt = bytes([67,68,69])
print(byt)
print(type(byt))
# byt[0] = 64
# print(byt)


b1 = bytearray([78,56])
print(b1)
b1[0] = 90
print(b1)
