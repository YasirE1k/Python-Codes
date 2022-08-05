#These codes can be wrong
import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.count=0
        self.button=QtWidgets.QPushButton("Press me")
        self.label=QtWidgets.QLabel("0 Click")
        
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.label)
        v_box.addStretch()

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)

        self.show()

        sys.exit(app.exec_())
    
    def click(self):
        self.count+=1
        self.label.setText(str(self.count)+" "+"Click")
        
app=QtWidgets.QApplication(sys.argv)        

a=Window()

        
