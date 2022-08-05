#These codes can be wrong
import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.question=QLabel("Which Language do you like most?")
        self.writing_area=QLabel("")
        self.button=QPushButton("Send")

        self.Java=QRadioButton("Java")
        self.Php=QRadioButton("Php")
        self.Python=QRadioButton("Python")

        v_box=QVBoxLayout()
        v_box.addWidget(self.question)
        v_box.addWidget(self.Java)
        v_box.addWidget(self.Php)
        v_box.addWidget(self.Python)
        v_box.addStretch()
        v_box.addWidget(self.writing_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("Radio Button")

        self.button.clicked.connect(lambda: self.click(self.Java.isChecked(),self.Python.isChecked(),self.Php.isChecked(),self.writing_area))
        self.show()
        sys.exit(app.exec_())
    
    def click(self,Java,Python,Php,writing_area):
        if(Java):
            writing_area.setText("Java")
        if(Python):
            writing_area.setText("Python")
        if(Php):
            writing_area.setText("Php")

app=QApplication(sys.argv)

a=window()
