import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QSizePolicy)

class Scene2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.middle_layout = QHBoxLayout()

        self.Time_Box()
        self.Recent_Box()
        self.Statics_Box()
        
        self.vbox.insertLayout(1, self.middle_layout)

    def Time_Box(self):
        self.time_box = QWidget()
        

        self.time_text = QLabel("00:00", self)
        self.time_text.setAlignment(Qt.AlignCenter)

        self.time_layout = QVBoxLayout(self.time_box)
        self.time_layout.addWidget(self.time_text)

        self.vbox.insertWidget(0, self.time_box)


        self.time_text.setStyleSheet("font: 30px;")

        self.time_box.setObjectName("TimerFrame")
        self.time_box.setFixedHeight(50)

    def Recent_Box(self):
        self.recent_box = QWidget()

        self.recent_text = QLabel("Recent Activity", self)
        self.recent_text.setAlignment(Qt.AlignCenter)

        self.recent_layout = QVBoxLayout(self.recent_box)
        self.recent_layout.addWidget(self.recent_text)


        self.recent_text.setStyleSheet("font: 30px;")
        self.recent_box.setObjectName("RecentFrame")

        self.middle_layout.addWidget(self.recent_box)

    def Statics_Box(self):
        self.statics_box = QWidget()

        self.statics_text = QLabel("Statistics", self)
        self.statics_text.setAlignment(Qt.AlignCenter)

        self.statics_layout = QVBoxLayout(self.statics_box)
        self.middle_layout.addLayout(self.statics_layout)
        self.statics_layout.addWidget(self.statics_text)


        self.statics_text.setStyleSheet("font: 30px;")
        self.statics_box.setObjectName("StaticsFrame")

        self.middle_layout.addWidget(self.statics_box)


    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout(self)

        self.setLayout(self.vbox)

        self.focus_button = QPushButton("Focus", self)
        self.add_button = QPushButton("Add Subject", self)
        self.return_button = QPushButton("Return", self)


        self.hbox.addWidget(self.return_button)
        self.hbox.addWidget(self.add_button)
        self.hbox.addWidget(self.focus_button)

        self.vbox.addLayout(self.hbox)


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
            #StaticsFrame {
                border: 2px solid green;
                border-radius: 3px;
                        }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Scene2()
    window.show()
    sys.exit(app.exec_()) 