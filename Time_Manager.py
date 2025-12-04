import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                        QLabel, QTextEdit, QHBoxLayout, QVBoxLayout, QStackedWidget)
from main_scenes import Scene1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager")
        self.setGeometry(800,500,800,500)
        self.initUI()

    def initUI(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_scene = Scene1()

        self.stack.addWidget(self.main_scene)
        self.stack.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 