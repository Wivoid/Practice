from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QScrollArea,
                             QLabel, QHBoxLayout, QPushButton)
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os

class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.style()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.top_bar = QVBoxLayout()
        self.scroll_area = QScrollArea()
        
        self.contentbox = QWidget()
        self.return_btn = QPushButton()


        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.addLayout(self.top_bar)
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)


        self.top_bar.addWidget(self.return_btn, alignment=Qt.AlignTop | Qt.AlignRight)

        self.scroll_area.setFrameShape(QScrollArea.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.contentbox)
        

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()


        self.vbox.setContentsMargins(20,30,20,40)
        self.contentbox.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox)
        

        self.title = QLabel("TIME MANAGER")
        self.version = QLabel("v1.0.4")
        self.info = QLabel("Info")
        self.question1 = QLabel("What's the purpose?")
        self.information1 = QLabel()
        self.question2 = QLabel("What can it do?")
        self.information2 = QLabel()
        self.question3 = QLabel("How to use it?")

        self.information1.setText("""<p style="line-height:130%;"> 
                                  The program is designed to be your own bridge which will follow your passion <br>
                                and help you with focusing on studying while maintaining high involvement. <br>
                                <br>
                                Also, it's a project of mine that was created to reinforce my Python knowledge <br>
                                while trying to build something big enough to be interesting
                                  </p>""")

        self.information2.setText("""
                                  <p style="line-height:140%; font-size: 24px;">
                                  Time Manager has something to serve for you, such as: 
                                  </p>

                                 <p style="line-height:120%;">
                                 • Settable focus time <br>
                                 • Changable task's name <br>
                                 • Sound reminder after finishing focus time <br>
                                 • Relaxing design <br>
                                 And much more soon
                                  </p>""")


        self.hbox.addStretch(36)
        self.hbox.addWidget(self.title, alignment=Qt.AlignCenter)
        self.hbox.addWidget(self.version, alignment=Qt.AlignCenter)
        self.hbox.addStretch(34)
        self.vbox.addSpacing(20)
        self.vbox.addWidget(self.info, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(10)
        self.vbox.addWidget(self.question1, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.information1, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(30)
        self.vbox.addWidget(self.question2, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.information2, alignment=Qt.AlignCenter)
        self.vbox.addStretch(4)


    def style(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.return_btn.setIcon(QIcon("prog/files/media/return.png"))
        self.return_btn.setIconSize(QtCore.QSize(30,30))

        self.info.setObjectName("Info")
        self.title.setObjectName("Title")
        self.version.setObjectName("Version")
        self.question1.setObjectName("Question")
        self.information1.setObjectName("Information")
        self.question2.setObjectName("Question")
        self.information2.setObjectName("Information")

        self.setStyleSheet("""

            QWidget {
                background-color: hsl(210, 89%, 92%);
            }

            QLabel {
                font-size: 20px;
            }
                           
            QPushButton{
                min-height:45px;
                min-width:50px;
                margin-top: 10px;
                margin-right: 10px;
                padding-bottom: 3px;
                background-color: hsl(209, 87%, 86%);
                border: 4px outset hsl(209, 25%, 60%);
                border-radius: 15px;
            }
                           
            QPushButton:hover {
                    color: hsl(209, 45%, 60%);
                    background-color: hsl(209, 70%, 83%);
            }
                           
            QScrollBar::vertical {
                background-color: hsl(210, 85%, 89%);
                border-radius: 8px;
                margin-bottom: 5px;
            }

            QScrollBar::handle:vertical{
                min-width: 22px;
                margin: 0px;
                border-radius: 8px;
                background: hsl(209, 87%, 84%);
                padding-bottom: 5px;
            }

            QScrollBar::handle:vertical::hover{
                background: hsl(209, 80%, 78%)
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, 
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
                background: none;
                height: 0px;
                width: 0px;
            }

            #Title {
                font-size: 60px;
                font-weight: bold;
            }

            #Version {
                font-size: 15px; 
                color: grey; 
                padding-top: 35px;
            }

            #Info {
                font-size: 40px;
            }
                           
            #Question {
                font-size: 30px;
            }
                           
            #Information {
                margin-top: 13px;
            }
        """)