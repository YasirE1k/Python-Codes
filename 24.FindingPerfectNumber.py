number=int(input("Enter a number"))
total=0
for x in range(1,number+1):
    if(number%x==0):
        total=total+x

if(total/2==number):
    print("Number is perfect")
else:
    print("It isn't")    
