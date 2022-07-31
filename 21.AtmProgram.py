balance=1000

print("Press q to exit")
print("1.Asking\n2.Pulling\n3.Putting")
while True:
    prcss=input("Enter process")
    if(prcss=="q"):
        break
    elif(prcss=="1"):
        print("Balance is {}".format(balance))
    elif(prcss=="2"):
        a=int(input("Enter amount"))
        balance=balance-a
    elif(prcss=="3"):
        b=int(input("Enter amount"))
        balance=balance+b
    else:
        print("Choose 1-2-3 or q")    


