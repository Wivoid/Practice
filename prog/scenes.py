import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QTextEdit, QHBoxLayout, QVBoxLayout)

class Scene2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.Time_Box()

    def Time_Box(self):
        self.focus_box = QWidget()
        self.recent_box = QWidget()
        self.statics_box = QWidget()


        self.middle_layout = QHBoxLayout()

        # Time-Box

        self.time_text = QLabel("00:00", self)
        self.time_text.setAlignment(Qt.AlignCenter)

        self.time_layout = QVBoxLayout(self.focus_box)
        self.time_layout.addWidget(self.time_text)
        
        
        # Recent-Box

        self.recent_text = QLabel("Recent Activity", self)
        self.recent_text.setAlignment(Qt.AlignCenter)

        self.recent_layout = QVBoxLayout(self.recent_box)
        self.recent_layout.addWidget(self.recent_text)

        # Statics-Box

        self.statics_text = QLabel("Statistics", self)
        self.statics_text.setAlignment(Qt.AlignCenter)

        self.statics_layout = QVBoxLayout(self.statics_box)
        self.middle_layout.addLayout(self.statics_layout)
        self.statics_layout.addWidget(self.statics_text)


        self.middle_layout.addWidget(self.statics_box)
        self.middle_layout.addWidget(self.recent_box)

        #Connections

        self.focus_box.setObjectName("TimerFrame")
        self.recent_box.setObjectName("RecentFrame")
        self.statics_box.setObjectName("StaticsFrame")


        self.time_text.setStyleSheet("font: 30px;")
        self.recent_text.setStyleSheet("font: 30px;")
        self.statics_text.setStyleSheet("font: 30px;")

        self.vbox.insertWidget(0, self.focus_box)
        self.vbox.insertLayout(1, self.middle_layout)

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