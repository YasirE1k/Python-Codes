import sqlite3

con=sqlite3.connect("libraryy.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf (name TEXT,writer TEXT,publisher TEXT, pageNumber INT)")
    con.commit()

createTable()
con.close()
