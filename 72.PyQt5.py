# Code1
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 1")

    window.show()

    sys.exit(app.exec_())

Window()
"""
#Code2
"""
import sys

from PyQt5 import QtWidgets,QtGui

def Window():

    app=QtWidgets.QApplication(sys.argv)

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 1")

    ticket1=QtWidgets.QLabel(window)
    ticket2=QtWidgets.QLabel(window)
    ticket2.setPixmap(QtGui.QPixmap("Python-PNG.png"))
    ticket1.setText("Here is a write")
    ticket1.move(200,30)
    ticket2.move(0,100)
    window.setGeometry(100,100,500,500)
    window.show()

    sys.exit(app.exec_())

Window()
"""

#Code3
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 3")

    button=QtWidgets.QPushButton(window)
    button.setText("Here is a button")
    ticket=QtWidgets.QLabel(window)
    ticket.setText("Hello World")

    ticket.move(200,30)
    button.move(180,80)

    window.setGeometry(100,100,500,500)
    
    window.show()

    sys.exit(app.exec_())

Window()
"""

#Code4
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)
    
    okay=QtWidgets.QPushButton("Okay")
    cancel=QtWidgets.QPushButton("Cancel")

    h_box=QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()   #it changes according to its location
    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 4")

    window.setLayout(h_box)

    window.setGeometry(100,100,500,500)
    
    window.show()

    sys.exit(app.exec_())

Window()
"""
#Code5
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)
    
    okay=QtWidgets.QPushButton("Okay")
    cancel=QtWidgets.QPushButton("Cancel")

    v_box=QtWidgets.QVBoxLayout()
    
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    v_box.addStretch()

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 4")

    window.setLayout(v_box)

    window.setGeometry(100,100,500,500)
    
    window.show()

    sys.exit(app.exec_())

Window()
"""

#Code6
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)
    
    okay=QtWidgets.QPushButton("Okay")
    cancel=QtWidgets.QPushButton("Cancel")

    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 4")

    window.setLayout(v_box)

    window.setGeometry(100,100,500,500)
    
    window.show()

    sys.exit(app.exec_())

Window()
"""

#Code 7 That I made tryings
"""
import sys

from PyQt5 import QtWidgets

def Window():

    app=QtWidgets.QApplication(sys.argv)
    
    okay=QtWidgets.QPushButton("Okay")
    cancel=QtWidgets.QPushButton("Cancel")

    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    window=QtWidgets.QWidget()

    window.setWindowTitle("PyQt5 Lesson 4")

    window.setLayout(h_box)

    window.setGeometry(100,100,500,500)
    
    window.show()

    sys.exit(app.exec_())

Window()
"""

#Code8
























