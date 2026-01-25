from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,
                             QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect,QApplication)
from PyQt5.QtGui import QColor, QBrush

import sys

class Scene1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.style()
        self.setAttribute(Qt.WA_StyledBackground, True)

    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.hbox.setSpacing(50)
        self.setLayout(self.vbox)

        self.vbox.addStretch(4)

        self.hello_text = QLabel("Hello", self)
        self.start_button = QPushButton("Start", self)
        self.info_button = QPushButton("Info", self)

        self.hbox.addWidget(self.info_button)
        self.info_button.setMinimumSize(200,80)
        self.info_button.setMaximumSize(800,100)

        self.hbox.addWidget(self.start_button)
        self.start_button.setMinimumSize(200,80)
        self.start_button.setMaximumSize(800,80)

        self.vbox.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.hello_text.setFixedSize(310,100)
        self.hello_text.setAlignment(Qt.AlignCenter)

        self.vbox.addStretch(2)
        
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)

    def apply_shadow(self, widget):
        
        shadow = QGraphicsDropShadowEffect()
        if widget == self.hello_text:
            color = (QColor(0,0,100,50))
            shadow.setBlurRadius(30)
        else:
            color = (QColor(0,0,100,110))
            shadow.setBlurRadius(50)
        shadow.setXOffset(5)
        shadow.setYOffset(5)

        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)

    def style(self):
        

        self.apply_shadow(self.info_button)
        self.apply_shadow(self.start_button)
        self.apply_shadow(self.hello_text)

        self.setStyleSheet("""
            QWidget{
                    background-color: hsl(210, 89%, 92%);
                    }

            QPushButton {
                    margin-left: 30px;
                    margin-right: 30px;
                    font-size: 50px;
                    font-weight: bold;
                    color: hsl(209, 56%, 70%);
                    background-color: hsl(209, 87%, 86%);
                    border: 4px outset hsl(209, 25%, 63%);
                    border-radius: 15px;
                        }
                           
            QPushButton:hover {
                    color: hsl(209, 45%, 60%);
                    background-color: hsl(209, 70%, 83%);
                        }
                           
            QLabel {
                    border-radius: 20px;
                    color: #56728c;
                    font-size: 50px;
                    }
        """)