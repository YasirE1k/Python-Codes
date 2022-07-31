#Code1
"""
class squares():
    def __init__(self,maximum=0):
        self.maximum=maximum
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if(self.index<=self.maximum):
            return self.index**2
        else:
            self.index=0
            raise StopIteration
        
squares1=squares(5)
iteration=iter(squares1)

print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))
"""
"""
#Code2
def findPrimeNumber():
    for i in range(1,1001):
        if(i==1):
            pass
        elif(i==2):
            yield i
        else:
            counter=0
            list2=range(2,i)
            for k in range(0,len(list2)):
                if(i%list2[k]==0):
                    counter+=1
            if(counter==0):
                yield i
            else:
                pass 

for k in findPrimeNumber():
    print(k)
"""