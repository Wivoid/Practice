import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel ,QHBoxLayout
                             ,QApplication , QVBoxLayout,
                               QMenu, QSizePolicy, QMessageBox)
from ..windows.add_window import AddWindow
from .signal_values import subject_val

class Add_Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Subject")

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
        self.new_window.show()

        self.new_window.subj_send.connect(self.create_subj)

    def create_subj(self, name):
        self.subj = self.menu.addAction(name)

        self.subj.triggered.connect(lambda: self.subject_funct(name))

        self.setText(name)
        subject_val.value.emit(name)

    def subject_funct(self, name):
        self.setText(name)
        subject_val.value.emit(name)
        