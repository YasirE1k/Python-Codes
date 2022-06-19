"""
#Player saving program
#Code1
print("Player saving program")

name=input("Enter the name of the player:")
surname=input("Enter the surname of the player:")
team=input("Enter the team of the player:")

playerknowledges=[name,surname,team]
print("The name of the player: {}\nThe surname of the player:{} \nThe team of the player:{}".format(playerknowledges[0],playerknowledges[1],playerknowledges[2]))
"""
#Code2
#Finding the root of 2. degree 1 unknown equation 
#equation= ax^2+bx+c
a=int(input("Enter the value a:"))
b=int(input("Enter the value b:"))
c=int(input("Enter the value c:"))

delta=int((b**2)-(4*a*c))
x1=int((-b+(delta**(1/2)))/(2*a))
x2=int((-b-(delta**(1/2)))/(2*a))
print("x1 value:{} x2 value:{}".format(x1,x2))
