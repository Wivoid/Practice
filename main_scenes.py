import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QStackedWidget,
                        QLabel, QTextEdit, QHBoxLayout, QVBoxLayout)

class Scene1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.setLayout(self.vbox)

        self.hello_text = QLabel("Hello", self)
        self.hello_button = QPushButton("Hello", self)
        self.info_button = QPushButton("Info", self)

        self.hbox.addWidget(self.hello_text)
        self.hbox.addWidget(self.info_button)
        self.hbox.addWidget(self.hello_button)

        self.vbox.addStretch(3)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)


        self.setStyleSheet("""
            QPushButton {
                    font-size: 40px;
                        }
        """)