from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QLabel, QHBoxLayout)
from PyQt5.QtCore import Qt

class Info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.style()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.vbox.addLayout(self.hbox)
        self.setLayout(self.vbox)

        self.title = QLabel("TIME MANAGER")
        self.version = QLabel("v1.0.3")
        self.info = QLabel("Info")
        self.question1 = QLabel("What's the purpose?")
        self.information1 = QLabel()

        self.information1.setText("The program is designed to be your own bridge which will follow your passion"
                                "\n and help you with focusing on studying while maintaining high involvement"
                                "\n "
                                "\n Also, it's a project of mine that was created to reinforce my Python knowledge"
                                "\n while trying to build something big enough to be interesting")

        self.hbox.addStretch(2)
        self.hbox.addWidget(self.title, alignment=Qt.AlignCenter)
        self.hbox.addWidget(self.version, alignment=Qt.AlignCenter)
        self.hbox.addStretch(2)
        self.vbox.addSpacing(20)
        self.vbox.addWidget(self.info, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.question1, alignment=Qt.AlignCenter)
        self.vbox.addWidget(self.information1, alignment=Qt.AlignCenter)

        
        self.vbox.addStretch(4)



    def style(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(20,30,20,40)

        self.info.setObjectName("Info")
        self.title.setObjectName("Title")
        self.version.setObjectName("Version")
        self.question1.setObjectName("Question1")
        self.information1.setObjectName("Information1")

        self.setStyleSheet("""

            QWidget{
                background-color: hsl(210, 89%, 92%);
            }

            QLabel {
                font-size: 20px;
            }

            #Title {
                font-size: 50px;
                font-weight: bold;
            }

            #Version {
                font-size: 15px; 
                color: grey; 
                padding-top: 25px;
            }

            #Info{
                font-size: 40px;
            }
                           
            #Question1{
                font-size: 30px;
            }
                           
            #Information1{
                margin-top: 13px;
            }
        """)