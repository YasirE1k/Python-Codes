liste=["elma","mahmut",45,7.45]
print(type(liste))
liste2=[]
print(liste2)
liste3=list()
print(liste3)
print(len(liste))
liste4=list("merhaba")
print(liste4)
print(liste[2])
liste5=[1,2,3]
liste6=[4,5,6]
liste7=liste5+liste6
print(liste7)
print(3*liste5)
liste5[:2]=[20,31]
print(liste5)
liste8=[34,2]
liste5[:2]=liste8
print(liste5)

#liste metodlari galiba
#metod sadece listeler icin değil bircok veri tipi icin de kullanilabilir galiba

liste5.append("Python")
print(liste5)

print(liste5.pop())
print(liste5)
liste5.pop(0)
print(liste5)

#print(liste5.sort()) #yanlis kullanim galiba
liste5.sort()
print(liste5)
liste5.sort(reverse=True)
print(liste5)

liste9=[[1,2],[3,4],[5,6]]
print(liste9[2])




