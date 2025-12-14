import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel ,QHBoxLayout
                             ,QApplication , QVBoxLayout, QMenu)

class Add_Button(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.add_subject()

    def initUI(self):
        self.hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.setLayout(vbox)

        self.focus_button = QPushButton("Focus", self)
        self.add_button = QPushButton("Add Subject", self)
        self.return_button = QPushButton("Return", self)


        self.hbox.addWidget(self.return_button)
        self.hbox.addWidget(self.add_button)
        self.hbox.addWidget(self.focus_button)

        vbox.addLayout(self.hbox)


        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                        }
            #TimerFrame {
                border: 2px solid red;
                border-radius: 3px;
                        }
            #RecentFrame {
                border: 2px solid yellow;
                border-radius: 3px;
                            }
            #StatsFrame {
                border: 2px solid green;
                border-radius: 3px;
                            }
            """)

    def add_subject(self):
        menu = QMenu()

        menu_create = menu.addAction("Create")
        
        self.add_button.setMenu(menu)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Add_Button()
    window.show()
    sys.exit(app.exec_()) 