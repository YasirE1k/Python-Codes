fnumber=1
snumber=1
fibolist=[1,1]
for x in range(1,10):
    fnumber,snumber=snumber,fnumber+snumber
    fibolist.append(snumber)

print(fibolist)


