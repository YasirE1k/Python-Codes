#Programmer made the attention in the program. I made terminal
#These codes can be wrong
import sys
import sqlite3
from PyQt5 import  QtWidgets

class function(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.con=sqlite3.connect("UserEnterProject.db")

        self.cursor=self.con.cursor()

        def createTable():
            self.cursor.execute("CREATE TABLE IF NOT EXISTS userentering (user TEXT,password TEXT)")
            self.con.commit()
        createTable()
       
        self.username=QtWidgets.QLineEdit()
        self.password=QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter=QtWidgets.QPushButton("Enter")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addStretch()
        v_box.addWidget(self.enter)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("User Entering")

        self.enter.clicked.connect(self.click)

        self.show()
        
        sys.exit(app.exec_())
       
    def click(self):
        def taketheDatas():
            self.counter=0
            self.cursor.execute("Select * From userentering")
            self.list=self.cursor.fetchall()
        
            for self.i in self.list:
                if(self.i[0]==self.username.text() and self.i[1]==self.password.text()):
                    print("You entered")
                    self.counter=1
                    break
        
        taketheDatas()
        if(self.counter==0):
            print("Wrong username or password")
        
        
        #self.con.close()
        
app=QtWidgets.QApplication(sys.argv)

a=function()
