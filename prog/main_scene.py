from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,
                             QHBoxLayout, QVBoxLayout, QGraphicsDropShadowEffect,QApplication)
from PyQt5.QtGui import QColor

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
        self.hbox.addWidget(self.start_button)

        self.vbox.addWidget(self.hello_text)
        self.hello_text.setAlignment(Qt.AlignCenter)

        self.vbox.addStretch(2)
        
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)

    def apply_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setXOffset(5)
        shadow.setYOffset(5)

        color = (QColor(0,0,100,110))
        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)

    def style(self):
        self.apply_shadow(self.info_button)
        self.apply_shadow(self.start_button)

        self.setStyleSheet("""
            QWidget{
                    background-color: hsl(210, 89%, 92%);
                    }

            QPushButton {
                    margin-left: 30px;
                    margin-right: 30px;
                    font-size: 40px;
                    color: hsl(209, 20%, 28%);
                    background-color: hsl(209, 87%, 86%);
                    border: 4px outset hsl(209, 25%, 63%);
                    border-radius: 15px;
                        }
                           
            QPushButton:hover {
                    background-color: hsl(209, 70%, 83%);
                        }
                           
            QLabel {
                    color: #56728c;
                    font-size: 50px;
                    }
        """)