#These codes can be wrong
#I will check tomorrow
#Code1 I tried something
"""
import sys
import os
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QMainWindow,QWidget):
    def __init__(self):

        super().__init__()

        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)

        dosya_kaydet.setShortcut("Ctrl+S")

        temizle = QAction("Dosyayı Temizle",self)
        temizle.setShortcut("Ctrl+D")

        cikis = QAction("Çıkış",self)

        cikis.setShortcut("Ctrl+Q")
        
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)
        
        self.setWindowTitle("Metin Editörü")

        self.show()

    
    def yaziyi_temizle(self):
        self.yazi_alani.clear()

    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],"w") as file:

            file.write(self.yazi_alani.toPlainText())
    
    def response(self,action):

        if action.text() == "Dosya Aç":
            dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

            with open(dosya_ismi[0],"r") as file:
                self.yazi_alani.setText(file.read())

        elif action.text() == "Dosya Kaydet":
            dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

            with open(dosya_ismi[0],"w") as file:
                file.write(self.yazi_alani.toPlainText())
        elif action.text() == "Dosyayı Temizle":
                self.yazi_alani.clear()

        elif action.text() == "Çıkış":
            qApp.quit()

app = QApplication(sys.argv)

menu = Notepad()


sys.exit(app.exec_())
"""

#Code2

import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.writing_area=QTextEdit()
        self.clear=QPushButton("Clear")
        self.open=QPushButton("Open")
        self.save=QPushButton("Save")

        h_box=QHBoxLayout()
        
        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box=QVBoxLayout()
        v_box.addWidget(self.writing_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("Notepad")

        self.clear.clicked.connect(self.clearr)
        self.open.clicked.connect(self.openn)
        self.save.clicked.connect(self.savee)
        
        
    def clearr(self):
        self.writing_area.clear()
    def savee(self):
        file_name=QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))    
        with open(file_name[0],"w") as file:
            file.write(self.writing_area.toPlainText())

    def openn(self):
        file_name=QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(file_name[0],"r") as file:
            self.writing_area.setText(file.read())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window=Notepad()

        self.setCentralWidget(self.window)

        menubar=self.menuBar()

        file=menubar.addMenu("File")

        open_file=QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file=QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear=QAction("Clear File",self)
        clear.setShortcut("Ctrl+D")

        exit=QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear)
        file.addAction(exit)

        file.triggered.connect(self.response)

        self.setWindowTitle("Notepaddd")    

        self.show()

        sys.exit(app.exec())
    def response(self,action):
        if(action.text()=="Open File"):
            self.window.openn()
        elif(action.text()=="Save File"):
            self.window.savee()
        elif(action.text()=="Clear File"):
            self.window.clearr()
        elif(action.text()=="Exit"):
            qApp.quit()

app=QApplication(sys.argv)
a=Menu()
