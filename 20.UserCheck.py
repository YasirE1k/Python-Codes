syspassword="12345"
sysuser="john"

enteringright=3
while True:
    username=input("enter your username")
    password=input("enter your password")
    
    if (username==sysuser and password==syspassword):
        print("Completed")
    else:
        print("Username or Password is wrong")
        enteringright-=1
    if(enteringright==0):
        break

