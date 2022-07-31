#generally why self 
#The code that I made it can be wrong
import sqlite3
 
class book():
    def __init__(self):

        self.connecttodata()   #why self?
    
    def connecttodata(self):
        self.conn=sqlite3.connect("newlibrary.db")
        self.cursor=self.conn.cursor()      

        self.cursor.execute("create table if not exists bookshelf (name TEXT,writer TEXT,publisher TEXT,type TEXT,edition INT)")

    def showthebooks(self):
        self.cursor.execute("Select * From bookshelf")
        self.list7=self.cursor.fetchall()
        print("knowledges of bookshelf table")
        for l in self.list7:
            print(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+str(l[4]))
    
    def askthebook(self,name):
        self.w=0
        self.cursor.execute("Select * From bookshelf where name=?",(name,))
        self.list5=self.cursor.fetchall()
        for i in self.list5:
            print("Book name: {},Writer: {},Publisher:{},type:{},edition:{}".format(i[0],i[1],i[2],i[3],i[4]))
            self.w+=1
        if(self.w==0):
            print("There aren't in the library")
    def addthebook(self,x,y,z,t,u):    
        self.cursor.execute("Insert into bookshelf Values(?,?,?,?,?)",(x,y,z,t,u))
        self.conn.commit()
        print("The book was added")
    def deletebook(self,name):
        self.cursor.execute("Delete From bookshelf where name=?",(name,))
        self.conn.commit()
    def raisethepressure(self,name):
        self.cursor.execute("Select * From bookshelf where name=?",(name,))
        self.list6=self.cursor.fetchall()
            
        if(self.list6==[ ]):
            print("There isn't this book in the shelf")
        else:
            self.edition=self.list6[0][4]+1
            self.cursor.execute("Update bookshelf set edition = ? where name=?",(self.edition,name))
            self.conn.commit()
book1=book()

print("""***********************************
Welcome to the library program.
Process;
1. Show the books
2. Book asking
3. Add the book
4. Delete book 
5. Raise the pressure
Press q to exit.
***********************************""")

while True:
    choosing=input("Choose your process")
    if(choosing=="q"):
        print("Exited")
        break
    elif(choosing=="1"):
        book1.showthebooks()
    elif(choosing=="2"):
        book1.askthebook(input("enter name"))
    elif(choosing=="3"):
        namee=input("enter name")
        writerr=input("enter writer")
        publisherr=input("enter publisher")
        typee=input("enter type")
        editionn=int(input("enter edition"))
        
        book1.addthebook(namee,writerr,publisherr,typee,editionn)
    elif(choosing=="4"):
        book1.deletebook(input("enter name"))
    elif(choosing=="5"):    
        book1.raisethepressure(input("enter name"))
    else:
        print("Invalid process")





