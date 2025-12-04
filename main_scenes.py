import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QStackedWidget,
                        QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow)

class Scene1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800,500,800,500)
        self.initUI()

    def initUI(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addStretch(3)

        self.vbox.addLayout(self.hbox)
        self.stack.setLayout(self.vbox)

        self.vbox.addStretch(1)


        self.hello_text = QLabel("Hello", self)
        self.hello_button = QPushButton("Hello", self)
        self.info_button = QPushButton("Info", self)

        self.hbox.addWidget(self.hello_text)
        self.hbox.addWidget(self.info_button)
        self.hbox.addWidget(self.hello_button)



        self.stack.setStyleSheet("""
            QPushButton {
                    font-size: 40px;
                }
                                        
        """)