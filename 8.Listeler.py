list=["apple","alex",45,7.45]
print(type(list))
list2=[]
print(list2)
list3=list()
print(list3)
print(len(list))
list4=list("hello")
print(list4)
print(list[2])
list5=[1,2,3]
list6=[4,5,6]
list7=list5+list6
print(list7)
print(3*list5)
list5[:2]=[20,31]
print(list5)
list8=[34,2]
list5[:2]=list8
print(list5)

#list methods probably
#Method just isn't lists,it can use lots of data types probably too

list5.append("Python")
print(list5)

print(list5.pop())
print(list5)
list5.pop(0)
print(list5)

#print(list5.sort()) #using mistake probably
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)

list9=[[1,2],[3,4],[5,6]]
print(list9[2])




