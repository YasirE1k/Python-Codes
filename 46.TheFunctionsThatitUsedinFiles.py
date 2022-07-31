with open("knowledges.txt","r") as file:  #why are there the gaps?
    for i in file:
        print(i) 

with open("knowledges.txt","r") as file:
    print(file.tell())


with open("knowledges.txt","r") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())    


with open("knowledges.txt","r") as file:
    file.seek(5)
    content=file.read(10)
    print(content)


