#These codes can be wrong
import sys
from PyQt5 import  QtWidgets

class function(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.writingArea=QtWidgets.QLineEdit()
        self.clearr=QtWidgets.QPushButton("Clear")
        self.printt=QtWidgets.QPushButton("Print")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.writingArea)
        v_box.addWidget(self.clearr)
        v_box.addWidget(self.printt)
        v_box.addStretch()
        
        self.setLayout(v_box)

        self.clearr.clicked.connect(self.click)
        self.printt.clicked.connect(self.click)
        self.show()
        sys.exit(app.exec_())
    def click(self):
        sender=self.sender()
        if(sender.text()=="Clear"):
            self.writingArea.clear()
        else:
            print(self.writingArea.text())

app=QtWidgets.QApplication(sys.argv)

a=function()

