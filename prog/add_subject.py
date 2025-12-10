import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel,QHBoxLayout, 
                             QApplication, QVBoxLayout, QComboBox)

class Add_Button(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Add_Button()
    window.show()
    sys.exit(app.exec_()) 