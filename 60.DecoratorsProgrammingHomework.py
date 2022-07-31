def extra(func):
    def wrapper(numbers):
        for a in range(1,len(numbers)):
            total=0
            for b in range(1,a):
                if(a%b==0):
                    total=total+b
                else:
                    pass
            if(a==total):
                print(a)
            else:
                pass
        func(numbers)
    return wrapper

@extra
def findPrimeNumber(numbers):
    for i in numbers:
        if(i==1):
            pass
        elif(i==2):
            print(i)
        else:
            counter=0
            list2=range(2,i)
            for k in range(0,len(list2)):
                if(i%list2[k]==0):
                    counter+=1
            if(counter==0):
                print(i)
            else:
                pass                 #I used this first time

findPrimeNumber(range(1,1001))







