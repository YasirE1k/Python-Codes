sozluk1={"bir":1,"iki":2,"uc":3,"dort":4}
print(type(sozluk1))

print(sozluk1)
print(sozluk1["bir"])

sozluk1["bes"]=5
print(sozluk1)

sozluk2={"bir":[1,2,3,4],"iki":[[34,23],[354,1]],"uc":35}

print(sozluk2["iki"][1][1])
sozluk2["uc"]=45
print(sozluk2)

sozluk3={"sayilar":{"bir":1,"iki":2,"uc":3},"harfler":{"a":1,"b":2,"c":3}}

print(sozluk3["sayilar"])
print(sozluk3["sayilar"]["iki"])

print(sozluk3.keys()) #dict keys python bunu liste olarak kabul ediyo
print(sozluk3.values()) #dict values listelere cok benziyo
print(sozluk3.items()) #liste icindeki demet mi?







