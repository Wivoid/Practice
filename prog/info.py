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
        self.version = QLabel("v1.0.0")
        self.info = QLabel("Info")

        
        self.hbox.addStretch(2)
        self.hbox.addWidget(self.title, alignment=Qt.AlignCenter)
        self.hbox.addWidget(self.version, alignment=Qt.AlignCenter)
        self.hbox.addStretch(2)
        self.vbox.addSpacing(20)
        self.vbox.addWidget(self.info, alignment=Qt.AlignCenter)
        
        self.vbox.addStretch(4)



    def style(self):
        self.setContentsMargins(20,30,20,40)

        self.info.setObjectName("Info")
        self.title.setObjectName("Title")
        self.version.setObjectName("Version")

        self.setStyleSheet("""

            #Title {
                font-size: 50px;
                font-weight: bold;
            }

            #Version {
                font-size: 20px; 
                color: grey; 
                padding-top: 25px;
            }

            #Info{
                font-size: 30px;
            }
        """)