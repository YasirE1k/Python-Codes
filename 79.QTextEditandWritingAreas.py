#These codes can be wrong
import sys

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.writing_area=QTextEdit()
        self.button=QPushButton("Clear")

        v_box=QVBoxLayout()
        v_box.addWidget(self.writing_area)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle("QTextEdit")

        self.button.clicked.connect(self.click)
    
        self.show()

        sys.exit(app.exec())
    def click(self):
        self.writing_area.clear()

app=QApplication(sys.argv)

a=window()
