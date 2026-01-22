from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,QHBoxLayout, QVBoxLayout)

class Scene1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setAttribute(Qt.WA_StyledBackground, True)

    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.setLayout(self.vbox)

        self.vbox.addStretch(4)

        self.hello_text = QLabel("Hello", self)
        self.start_button = QPushButton("Start", self)
        self.info_button = QPushButton("Info", self)

        self.hbox.addWidget(self.info_button)
        self.hbox.addWidget(self.start_button)

        self.vbox.addWidget(self.hello_text)
        self.hello_text.setAlignment(Qt.AlignCenter)

        self.vbox.addStretch(2)

        
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)


        self.setStyleSheet("""
            QWidget{
                    background-color: #9dcefc;
                    }

            QPushButton {
                    font-size: 40px;
                    color: hsl(209, 20%, 28%);
                    border: 1.5px dashed #4c6175;
                    border-radius: 15px;

                        }
            QLabel {
                    color: #56728c;
                    font-size: 50px;       
                    }
        """)