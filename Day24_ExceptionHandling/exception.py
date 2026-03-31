# try:
#     print("Hello")
# except:
#     print("Testing....")
# finally:
#     print("Done😎")

# print("using zerodivision")
# try:
#     print(10/2)
# except:
#     print("No error")
# finally:
#     print("clear")
# print("Example witrh ZDE")
# try:
#     print(10/0)
#     print("exiting from the try block")
# except:
#     print("oops")
# finally:
#     print("clear")


# print("default exception")
# try:
#     print("In try block")
#     a = 10
#     b = 0
#     print(a/b)
# except ZeroDivisionError as e:
#     print("In excpetation block")
#     print(f"Error is {e}")

# print("Example using value error")
# try:
#     a = int(input("Enter the value: "))
# except ValueError as m:
#     print(f"Value error as {m}")
# print("Done")


print("Using mutiple erros")

# try:
#     a = int(input("Enter a value : "))
#     b = int(input("Enter b value : "))
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"ErrorType - {e}")
# except ValueError as v:
#     print(f"ErrorType-{v}")
# finally:
#     print("My part is to execute..")


print("generic error")
# try:
#     name = "Python"
#     print(name)
#     print(10/0)
# except Exception:
#     print("Exception error")
# except ZeroDivisionError:
#     print("Zero Divison error")


try:
    name = "Python"
    print(name)
    print(10/0)

except ZeroDivisionError:
    print("Zero Divison error")
except Exception:
    print("Exception error")
