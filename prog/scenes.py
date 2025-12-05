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
        self.time_box = QWidget()
        self.time_text = QLabel("00:00", self)
        self.time_text.setAlignment(Qt.AlignCenter)

        self.time_layout = QHBoxLayout(self.time_box)
        self.time_layout.addWidget(self.time_text)

        self.time_box.setObjectName("TimerFrame")
        self.time_text.setStyleSheet("font: 30px;")

        self.vbox.insertWidget(0, self.time_box)

    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout(self)

        self.setLayout(self.vbox)

        self.focus_button = QPushButton("Focus", self)
        self.return_button = QPushButton("Return", self)

        self.vbox.addStretch(1)

        self.hbox.addWidget(self.return_button)
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
        """)