def wish(greet):
    def wrapper(name):
        if name == "Tarannum":
            print("Hello", name, "Is absent today, she missed the Lastsession")
        else:
            greet(name)
    return wrapper
        


@wish
def greet(name):
    print("Name:", name)

greet("Fathima")
greet("Nikath")
greet("Tarannum")


print("------------------------------------------------")

def decor(python):
    def inner():
        print("It was a really great Jounery with you guys ❤️❤️❤️")
        python()
        print("Wishinh you a very good luck...🌟🌟🌟🌟🌟")
    return inner


@decor
def python():
    print("Last of python feeling heavy hearted😶‍🌫️😒")

python()



print("--------------------------------------")
def permission(funct):
    def inner(user):
        if user == "Admin":
             print("Only Admin's has the access...")
             funct(user)
        else:
            print("Invalid permission❌")
    return inner

       

@permission
def dashboard(user):
    print("Welcome:", user)
# dashboard(user = "Admin")
dashboard(user = "Guest")