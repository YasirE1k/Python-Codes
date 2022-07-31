#Code1
"""
import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

createTable()
con.close()
"""

#Code2
"""
import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

createTable() #is this unnecessary, do I need once 

def addData():
    cursor.execute("Insert into bookshelf Values('Istanbul Hatirasi','Ahmet Umit','Everest','561')")
    con.commit()

addData()

con.close()
"""

#Code3
"""
import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

createTable() #is this unnecessary, do I need once 

def addData():
    cursor.execute("Insert into bookshelf Values('Istanbul Hatirasi','Ahmet Umit','Everest','561')")
    con.commit()

def addData2(name,writer,publisher,page_number):
    cursor.execute("Insert into bookshelf Values(?,?,?,?)",(name,writer,publisher,page_number))
    con.commit()

name=input("Name")
writer=input("Writer")
publisher=input("Publisher")
page_number=int(input("Page Number"))

addData2(name,writer,publisher,page_number)

con.close()
"""

#Code4

import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

def addData():
    cursor.execute("Insert into bookshelf Values('Istanbul Hatirasi','Ahmet Umit','Everest','561')")
    con.commit()

def addData2(name,writer,publisher,page_number):
    cursor.execute("Insert into bookshelf Values(?,?,?,?)",(name,writer,publisher,page_number))
    con.commit()

def taketheDatas():
    cursor.execute("Select * From bookshelf ")
    list= cursor.fetchall()
    #print(list)
    print("knowledges of bookshelf table")
    for i in list:
        print(i)

def taketheDatas2():
    cursor.execute("Select name,writer From bookshelf")
    list2=cursor.fetchall()
    for j in list2:
        print(j)

#addData()
#taketheDatas()
#taketheDatas2()

def taketheDatas3(publisherr):
    cursor.execute("Select * From bookshelf where publisher=?",(publisherr,))
    list3=cursor.fetchall()
    for k in list3:
        print(k)

#taketheDatas3("Everest")

con.close()
"""

#Code5  I'm not sure from this code

"""
import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

def addData():
    cursor.execute("Insert into bookshelf Values('Istanbul Hatirasi','Ahmet Umit','Everest','561')")
    con.commit()

def addData2(name,writer,publisher,page_number):
    cursor.execute("Insert into bookshelf Values(?,?,?,?)",(name,writer,publisher,page_number))
    con.commit()

def taketheDatas():
    cursor.execute("Select * From bookshelf ")
    list= cursor.fetchall()
    #print(list)
    print("knowledges of bookshelf table")
    for i in list:
        print(i)

def taketheDatas2():
    cursor.execute("Select name,writer From bookshelf")
    list2=cursor.fetchall()
    for j in list2:
        print(j)

#taketheDatas()
#taketheDatas2()

def taketheDatas3(publisherr):
    cursor.execute("Select * From bookshelf where publisher=?",(publisherr,))
    list3=cursor.fetchall()
    for k in list3:
        print(k)

#taketheDatas3("Everest")

def updateDatas(old_publisher,new_publisher):
    cursor.execute("Update bookshelf set publisher = ? where publisher=?",(new_publisher,old_publisher))
    con.commit()

#updateDatas("Dogan Kitap","Everest")

def deleteDatas(writer):
    cursor.execute("Delete From bookshelf where writer=?",(writer,))
    con.commit()

deleteDatas("Ahmet Umit")

con.close()
"""























