"""
with open("knowledges.txt","r+") as file:
    print(file.read())

with open("knowledges.txt","r+") as file:
    content=file.read()
    content="John A\n"+content
    file.seek(0)
    file.write(content)
"""

"""
with open("knowledges.txt","r+") as file:
    list=file.readlines()
    list.insert(3,"Oliver V\n")
    print(list)
    file.seek(0)
    file.writelines(list)
    print(file.read())     #Do I have to a new with open to see the result in the terminal???

with open("knowledges.txt","r+") as file:
    print(file.read())
"""


with open("knowledges.txt","r+") as file:
    list=file.readlines()
    list.insert(3,"Oliver V\n")
    print(list)
    file.seek(0)
    for i in list:
        file.write(i)

with open("knowledges.txt","r+") as file:
    print(file.read())
    print(list)
