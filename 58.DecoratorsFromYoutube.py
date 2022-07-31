#These codes can be wrong I wrote
#I watched the youtube video randomly
"""
def decorator(func):
    def wrapper():
        print("Decorator runned")
        func()
        print("Decorator finished")
    return wrapper

def function():
    print("Function is running")

function3=decorator(function)

function3()
"""

"""
def decorator(func):
    def wrapper():
        print("Decorator runned")
        func()
        print("Decorator finished")
    return wrapper

@decorator
def function():
    print("Function is running")

function()
"""
"""
#Myself happened mix it can be wrong
import time
#youtube man made with args kwargs it was logical
def calculate_time(func):
    def wrapper(list):      
        starting=time.time()
        func(list)
        finishing=time.time()
        print(func.__name__,"worked",(finishing-starting),"second")
    return wrapper

@calculate_time
def take_square(list):
    for i in list:
        print(i*i) 

@calculate_time
def take_cubes(list):
    for c in list:
        print(c**3)

a=[1,2,3,4,5]
take_square(a)

take_cubes(a)
"""

#there is the return situation of the functions on video
















