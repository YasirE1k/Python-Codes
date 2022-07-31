#Code1 That I tried from my head

from re import L

with open("text.txt","r",encoding="utf-8") as file:
    words=file.read()
    print(words)
    words2=words.split()
    print(words2)
    list=[ ]
    for x in words2:
        x=x.strip()
        x=x.strip(".")
        x=x.strip(",")
        x=x.strip("-")
        list.append(x)
    print(list)

    dictionary=dict()

    for a in list:
        if(a in dictionary):
            dictionary[a]+=1
        else:
            dictionary[a]=1

    for k,n in dictionary.items():    #I can make this probably
        print("{} word passed {} times in the text".format(k,n))






