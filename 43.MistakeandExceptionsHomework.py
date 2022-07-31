"""
#Code1
list = ["345","sadas","324a","14","john"]

for x in list:
    try:
        print(int(x))
    except:
        print("This is not integer")
"""
"""
#Code2

def isitDoubleorSingle(value):
    if(value%2!=0):
        raise ValueError        #when the programmer made it happen, but when I made it didn't write 4 times. I didn't understand.
    print(value)    

list=[10,22,79,43,11,80]

for x in list:
    isitDoubleorSingle(x)

"""
