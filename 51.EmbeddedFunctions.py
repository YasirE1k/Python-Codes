#Problem-1
"""
def findArea(x):
    area=x[0]*x[1]
    return area

list=[(3,4),(10,3),(5,6),(1,9)]

for i in list:
    print(findArea(i))
"""
"""
list(map(lambda a : a[0]*a[1],[(3,4),(10,3),(5,6),(1,9)]))
print(list(map(lambda a : a[0]*a[1],[(3,4),(10,3),(5,6),(1,9)])))
"""

"""
def findArea(x):
    area=x[0]*x[1]
    return area

list(map(findArea,[(3,4),(10,3),(5,6),(1,9)]))
print(list(map(findArea,[(3,4),(10,3),(5,6),(1,9)])))
"""


#Problem-2
"""
list(filter(lambda x : abs(x[0]-x[1])<x[2]<abs(x[0]+x[1]) and abs(x[0]-x[2])<x[1]<abs(x[0]+x[2])and abs(x[2]-x[1])<x[0]<abs(x[2]+x[1]),[(3,4,5),(6,8,10),(3,10,7)]))
print(list(filter(lambda x : abs(x[0]-x[1])<x[2]<abs(x[0]+x[1]) and abs(x[0]-x[2])<x[1]<abs(x[0]+x[2])and abs(x[2]-x[1])<x[0]<abs(x[2]+x[1]),[(3,4,5),(6,8,10),(3,10,7)])))
"""


#Problem-3
"""
from functools import reduce

listt=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9,10]))

reduce(lambda x,y : x+y,list(filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9,10])))
print(reduce(lambda x,y : x+y,list(filter(lambda a : a%2==0,[1,2,3,4,5,6,7,8,9,10]))))
"""

#Problem-4
"""
names=["John","Alex","Emily","Robert","Jack","Bob","Julia"]
surnames=["Brown","Dean","Thought","Black","Wizard","Honest","North"]

list(zip(names,surnames))
print(list(zip(names,surnames)))

for i in list(zip(names,surnames)):
    print(i[0]+" "+i[1])
"""










