"""
try:
    print(int("sadsaddsad13213"))
except:
    print("It happened a mistake")
print("Blocks finished")

try:
    print(int("sadsaddsad13213"))
except ValueError:
    print("It happened a mistake")
print("Blocks finished")


try:
    a=int(input("enter number1"))
    b=int(input("enter number2"))
    print(a/b)
except (ValueError,ZeroDivisionError):
    print("You made ValueError or ZeroDivisionError mistake")


try:
    a=int(input("enter number1"))
    b=int(input("enter number2"))
    print(a/b)
except ValueError:
    print("You made ValueError")
except ZeroDivisionError:
    print("You made ZeroDivisionError")


try:
    a=int(input("enter number1"))
    b=int(input("enter number2"))
    print(a/b)
except ValueError:
    print("You made ValueError")
except ZeroDivisionError:
    print("You made ZeroDivisionError")    
finally:
    print("Here worked")
"""
"""
def turnreverse(x):
    if(x!=str):
        raise ValueError("Please enter a true input")
    return x[::-1]

print(turnreverse(57))
"""


def turnreverse(x):
    
    return x[::-1]

try:
    print(turnreverse(67))
    print("True value")
except ValueError:           #Why didn't it write just Wrong Value??? 
    print("Wrong Value")
