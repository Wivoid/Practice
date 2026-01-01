import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QStackedWidget)
from prog.main_scene import Scene1
from prog.scenes import Scene2
from prog.scenes import Scene3
from prog.files.subj_value import Val

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager")
        self.setGeometry(800,500,800,500)
        self.setMinimumSize(500,300)
        self.initUI()

        self.current_subj = ""

    def initUI(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_scene = Scene1()
        self.menu_scene = Scene2()
        self.focus_scene = Scene3()

        self.stack.addWidget(self.main_scene)
        self.stack.addWidget(self.menu_scene)
        self.stack.addWidget(self.focus_scene)

        
        self.stack.setCurrentIndex(0)

        self.menu_scene.return_button.clicked.connect(self.Return)
        self.main_scene.start_button.clicked.connect(self.Menu)
        self.menu_scene.focus_button.clicked.connect(self.Focus)

        Val.value.connect(self.save_subj)

    def Return(self):
        self.stack.setCurrentIndex(0)

    def Menu(self):
        self.stack.setCurrentIndex(1)

    def Focus(self):
        hours = self.menu_scene.h_time.value()
        minutes = self.menu_scene.min_time.value()


        self.focus_scene.set_time(hours, minutes)

        if self.current_subj == '':
            QMessageBox.warning(self, 'Warning!', 'Please select subject')
        else:
            self.stack.setCurrentIndex(2)
        
    def save_subj(self, name):
        self.current_subj = name

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 