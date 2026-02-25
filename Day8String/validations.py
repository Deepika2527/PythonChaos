sent = "Your password is 4768"
print(sent.isalpha())
print(sent.isalnum())
sent1 = "welcomeat"
print(sent1.isalpha())
print("aplanum without space")
print("Welcom123".isalnum())

print("Isdecimal will get only true if it has no's fro 0-9")
n = "1234"
print(n.isdecimal())
n1 = "-1234"
print(n1.isdecimal())
print("Ⅹ".isdecimal())
print("⁰".isdecimal())
print("½".isdecimal())

print("Isnumeric returns T for no's,Romanno, fractions and superscript ")
print("123".isnumeric())
print("-123".isnumeric())
print("Ⅹ".isnumeric())
print("⁰".isnumeric())
print("½".isnumeric())

print("Isdigit return T for no's,super")
print("123".isdigit())
print("-123".isdigit())
print("Ⅹ".isdigit())
print("⁰".isdigit())
print("½".isdigit())



print(isinstance("12",str))
print(isinstance(12,str))


