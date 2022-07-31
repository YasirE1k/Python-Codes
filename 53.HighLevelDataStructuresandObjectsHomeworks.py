#Problem-1
"""
a="ProgrammingHomeworkHighLevelDataStructuresandObjectspynb"

print(a.count("a"))
"""
#Problem-2
"""
with open("poem.txt","w",encoding="utf-8") as file:
    list=["Memlekete sis çökmüş bir gece 
Usulca yanağıma sen düşüyorsun
Sabah saat dokuzu beş geçe
Terk edip bizleri gidiyorsun
Ayrılık bu kadar yakmamıştı içimizi
Farkında mısın bilmiyorum
Aldın beraberinde cumhuriyetimizi
Korkunç bir veda, sararmıştı her yer
Ellerini uzat tutmak istiyoruz
Masmavi gözleri kaybetmiş çocuk
Aldı bir sabah ruhumuzu
Lakin nasıl bölmesin yokluğun uykumuzu"]
    a=[ ]
    n = ""          #new thing
    for x in list:
        file.write(x)
        b=x.split("\n")
    print(b)
    for i in b:
        a.append(i[0])
    print(a)
    for k in a:
        n+=k
    print(n)
"""

#Problem-3
"""
#I will read the line
with open("mails.txt","r",encoding="utf-8") as file:

    for i in file:
        i=i[:-1]
        if(i.endswith(".com") and i.find("@")!=-1):
            print(i)
"""

#Problem-4
"""
names=["John","Alex","Emily","Robert","Jack","Bob","Julia"]
surnames=["Brown","Dean","Thought","Black","Wizard","Honest","North"]

list(zip(names,surnames))
list2=[ ]
for x in list(zip(names,surnames)):
    list2.append(x[0]+" "+x[1])
print(list2)
list2.sort()
print(list2)
for c in list2:
    print(c)
"""









    










    



