#These codes can be wrong

import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.checkbox=QCheckBox("Do you like Python?")
        self.writingarea=QLabel("")
        self.button=QPushButton("Click me")

        v_box=QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addStretch()
        v_box.addWidget(self.writingarea)
        v_box.addStretch()
        v_box.addWidget(self.button)
        
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Check Box")

        self.button.clicked.connect(lambda: self.click(self.checkbox.isChecked(),self.writingarea))

        self.show()
        sys.exit(app.exec_())
    
    def click(self,checkbox,writingarea):
        if(checkbox):
            writingarea.setText("You like Python, very nice")
        else:
            writingarea.setText("Why don't you like")

app=QApplication(sys.argv)

a=window()


