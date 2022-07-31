#when I took file.txt it write I didn't understand anything.

def calculateNote(line):
    list1=[ ]
    
    list1=line.split(",")
    

    name=list1[0]
    note1=int(list1[1])
    note2=int(list1[2])
    note3=int(list1[3])

    last_note = note1 * (3/10) + note2 * (3/10) + note3 * (4/10)

    if (last_note >= 90):

        letter = "AA"
    elif (last_note >= 85):
        letter = "BA"
    elif (last_note >= 80):
        letter = "BB"
    elif (last_note >= 75):
        letter = "CB"
    elif (last_note >= 70):
        letter = "CC"
    elif (last_note >= 65):
        letter = "DC"
    elif (last_note >= 60):
        letter = "DD"
    elif (last_note >= 55):
        letter = "FD"
    else:
        letter = "FF"


    return name + "---------->" + letter + "\n"

with open("pytnfileexecsie.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list4=[ ]
    for i in list:
        list4.append(calculateNote(i))
        
with open("file.txt","w",encoding="utf-8") as file:
    for x in list4:
        file.write(x)







