"""
#Code1

print(*******************
This is a calculator 
App

+-*/

)

x=int(input("Enter 1. number:"))
y=int(input("Enter 2. number:"))

a=input("Choose an operator:")

if(a=="+"):
    print("{} and {} total: {}".format(x,y,x+y))
elif(a=="-"):
    print("{} and {} difference: {}".format(x,y,x-y))
elif(a=="*"):
    print("{} and {} multiplication: {}".format(x,y,x*y))
elif(a=="/"):
    print("{} and {} divide: {}".format(x,y,x/y))
else:
    print("You entered wrong operator")

"""
"""
#Code2
#Pairing name password
thepasswordinthesystem="123456"
usernameinthesystem="john"

name=input("Enter the username:")
password=input("Enter the password:")

if(name==usernameinthesystem and password!=thepasswordinthesystem):
    print("password is wrong")
elif(name!=usernameinthesystem and password==thepasswordinthesystem):
    print("Username is wrong")
elif(name!=usernameinthesystem and password!=thepasswordinthesystem):
    print("Username and password is wrong")
else:
    print("Congrulations you entered...")
"""
"""
#Kod3
#triangle rectangle 
type=input("Which of them do you want to find the type of triangle or rectangle:")

if(type=="ordinarysquare"):
    edge1=int(input("Enter 1. edge:"))
    edge2=int(input("Enter 2. edge:"))
    edge3=int(input("Enter 3. edge:"))
    edge4=int(input("Enter 4. edge:"))
    if(edge1==edge2==edge3==edge4):
        print("This is a square")
    elif((edge1==edge2 and edge3==edge4) or (edge1==edge3 and edge2==edge4) or (edge1==edge4 and edge2==edge3)):
        print("This is a rectangle")
    else:
        print("This is a ordinary square")
elif(type=="triangle"):
    edge5=int(input("Enter 1. edge:"))
    edge6=int(input("Enter 2. edge:"))
    edge7=int(input("Enter 3. edge:"))
    if(abs(edge5-edge6)<edge7<edge5+edge6 and abs(edge5-edge7)<edge6<edge5+edge7 and abs(edge6-edge7)<edge5<edge6+edge7):
        if(edge5==edge6==edge7):
            print("equilateral triangle")
        elif((edge5==edge6 and edge5!=edge7) or (edge7==edge5 and edge7!=edge6) or (edge6==edge7 and edge6!=edge5)):
            print("isosceles triangle")
        elif(edge5!=edge6 and edge5!=edge7 and edge6!=edge7):
            print("ordinary triangle")
    else:
        print("It isn't indicate triangle")
else:
    print("Please enter true input...")    
"""













