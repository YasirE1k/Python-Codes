def isitPrime(number):
    if(number==0 or number==1):
        return False
    elif(number==2):
        return True
    else:
        for i in range(2,number):
            if(number%i==0):
                return False
    return True        

print(isitPrime(71))

"""
def total(a,b,c):
    print("Total function") # worked.
    return a + b + c

total(1,2,3)  #Probably in jupyternotebook it wrote but didn't happen here
                #ı'm not sure
"""




