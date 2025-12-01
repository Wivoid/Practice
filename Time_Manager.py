import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                        QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager")
        self.setGeometry(800,500,800,500)
        self.initUI()

    def initUI(self):
        self.central_widg = QWidget()
        self.setCentralWidget(self.central_widg)

        self.grid = QGridLayout(self.central_widg)
        self.grid.setColumnStretch(0,1)
        self.grid.setColumnStretch(3,1)

        self.hello_button = QPushButton("Hello", self)
        self.info_button = QPushButton("Info", self)

        self.central_widg.setStyleSheet("""
            QPushButton {
                    font-size: 40px;
                }
                                        
        """)

        self.grid.addWidget(self.info_button, 1,1,1,1, Qt.AlignCenter)
        self.grid.addWidget(self.hello_button, 1,2,1,1, Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 