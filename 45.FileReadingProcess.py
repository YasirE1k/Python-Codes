file=open("knowledges.txt","r")

file.close()

file=open("knowledges.txt","r")

for i in file:
    print(i, end = "" )

file.close()

file=open("knowledges.txt","r")

content=file.read()
print("File Content...")

print(content)

file=open("knowledges.txt","r")
print(file.readline())
file.close()


file=open("knowledges.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file=open("knowledges.txt","r")

list=file.readlines()
print(list)
file.close()





















