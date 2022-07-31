import random 
import time 

randomnumber=random.randint(1,100)
right=10
while True:
    number=int(input("Enter the number"))
    if(number>randomnumber):
        print("Enter low value")
        right-=1
    elif(number<randomnumber):
        print("Enter high value")
        right-=1
    else:
        print("Congrucalitons you found")
        break
    if(right==0):
        print("Game over")
        break
