import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import pyqtSignal, Qt
import time

class AddWindow(QWidget):
    subj_send = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subject Adding")
        self.setMinimumSize(350,150)
        self.initUI()
        self.style()
    
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


        Submit.clicked.connect(self.btn_submit)
        Return.clicked.connect(self.btn_return)
        
    def btn_submit(self):
        if self.Input.text() != '':
            subj_name = self.Input.text()
            self.subj_send.emit(subj_name)
            time.sleep(0.3)
            self.close()
        else:
            QMessageBox.warning(self, "Subject Name Warning", "Please enter your subject name")

    def btn_return(self):
        self.close()


    def style(self):
        self.Input.setObjectName("Input")

        self.setStyleSheet("""
            QPushButton {
                font-size: 25px;
                font-weight: bold;
                color: hsl(209, 56%, 70%);
                background-color: hsl(209, 87%, 86%);
                border: 3px outset hsl(209, 25%, 60%);
                border-radius: 14px;
            }
                           
            QMessageBox QPushButton{
                padding: 5px;
            }
                        
            QMessageBox QLabel{
                font-size: 20px;
                font-weight: bold;
                color: hsl(209, 51%, 52%);
            }
                           
            QPushButton::hover {
                color: hsl(209, 56%, 70%);
                background-color: hsl(209, 87%, 89%);
            }
                
            QLineEdit#Input {
                font-size: 20px;
                border: 3px dashed hsl(209, 40%, 70%);
                border-radius: 7px;
                background: hsl(210, 89%, 89%);
            }
                           
            QWidget{
                background: hsl(210, 89%, 92%);
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddWindow()
    window.show()
    sys.exit(app.exec_()) 