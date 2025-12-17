import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel ,QHBoxLayout
                             ,QApplication , QVBoxLayout, QMenu, QSizePolicy, QMessageBox)
from .add_window import AddWindow

class Add_Button(QPushButton):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.setText("Subject")
=======
        self.setText("Add Subject")
>>>>>>> afe7fd335ddad42c600db3f8c58ce4453fb0833b

        self.menu = QMenu()
        self.menu.setStyleSheet("font-size: 20px;")
        self.menu.aboutToShow.connect(self.update_button)

        self.add_subject()

    def add_subject(self):
        self.menu_create = self.menu.addAction("Create")
        self.menu_create.triggered.connect(self.add_funct)
        self.setMenu(self.menu)

    def update_button(self):
        self.menu.setMinimumWidth(self.width())
        
    def add_funct(self):
        self.new_window = AddWindow()
<<<<<<< HEAD
        self.new_window.show()

        self.new_window.subj_send.connect(self.create_subj)

    def create_subj(self, name):
        subj = self.menu.addAction(name)
=======
        self.new_window.show()
>>>>>>> afe7fd335ddad42c600db3f8c58ce4453fb0833b
