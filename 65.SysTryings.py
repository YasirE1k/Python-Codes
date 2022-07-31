#I made
import sys

counter=0
value=0
for i in (sys.argv):
    if(i!="5" and value==1):
        counter=1
        break
    value=1
if(counter==1):    
    sys.stderr.write("You didn't enter all values 5")
    sys.stderr.flush()
else:
    sys.stdout.write("Congrulations")

