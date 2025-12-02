import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                        QLabel, QTextEdit, QHBoxLayout, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager")
        self.setGeometry(800,500,800,500)
        self.initUI()

    def initUI(self):
        self.central_widg = QWidget()
        self.setCentralWidget(self.central_widg)

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addStretch(3)

        self.vbox.addLayout(self.hbox)
        self.central_widg.setLayout(self.vbox)

        self.vbox.addStretch(1)


        self.hello_button = QPushButton("Hello", self)
        self.info_button = QPushButton("Info", self)

        self.hbox.addWidget(self.info_button)
        self.hbox.addWidget(self.hello_button)



        self.central_widg.setStyleSheet("""
            QPushButton {
                    font-size: 40px;
                }
                                        
        """)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 