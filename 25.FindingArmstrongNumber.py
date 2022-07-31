number=input("Enter the number")
total=0
for x in range(0,len(number)):
    total=total+int(number[x])**len(number) 

if(total==int(number)):
    print("Armstrong Number")
else:
    print("Not")

















