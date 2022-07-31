list3=[ ]
list4=[ ]
list5=[ ]
def seperate(knowledges):
    list2=[ ]
    knowledges=knowledges[:-1]     #I understood probably 

    list2=knowledges.split(",")
    for j in list2:
        if(j=="Galatasaray"):
            list3.append(list2[0]+" "+list2[1]+"\n")
        elif(j=="Fenerbahce"):
            list4.append(list2[0]+" "+list2[1]+"\n")
        elif(j=="Besiktas"):
            list5.append(list2[0]+" "+list2[1]+"\n")
       
with open("footballplayers.txt","w",encoding="utf-8") as file:
    list=["Fernando Muslera,Galatasaray\n",
    "Atiba Hutchinson,Besiktas\n",
    "Simon Kjaer,Fenerbahce\n",
    "Alex Teixeira,Besiktas\n",
    "Mostafa Mohamed,Galatasaray\n",
    "Marcao,Galatasaray\n"]
    for x in list:
        file.write(x)
    for y in list:
        seperate(y)

with open("gs.txt","w",encoding="utf-8") as file1:
    for t in list3:
        file1.write(t)
with open("fb.txt","w",encoding="utf-8") as file2:
    for z in list4:
        file2.write(z)
with open("bjk.txt","w",encoding="utf-8") as file3:
    for c in list5:
        file3.write(c)
