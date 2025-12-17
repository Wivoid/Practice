import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import pyqtSignal, Qt
import time

class AddWindow(QWidget):
    subj_send = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subject Adding")
        self.setMinimumSize(300,150)
        self.initUI()
    
    def initUI(self):
        self.Input = QLineEdit()
        Submit = QPushButton("Submit")
        Return = QPushButton("Return")

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.Input.setPlaceholderText("Your subject name")

        self.vbox.addWidget(self.Input)
        self.vbox.addWidget(Submit)


        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)

        self.hbox.addWidget(Return)
        self.hbox.addWidget(Submit)

        self.setStyleSheet("""
                QPushButton {
                        font-size: 25px;
                    }
                
                QLineEdit {
                        font-size: 20px;
                    }
        """)

        Submit.clicked.connect(self.btn_submit)
        
    def btn_submit(self):
        subj_name = self.Input.text()
        self.subj_send.emit(subj_name)
        time.sleep(0.3)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddWindow()
    window.show()
    sys.exit(app.exec_()) 