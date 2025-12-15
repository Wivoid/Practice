import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,QLabel ,QHBoxLayout
                             ,QApplication , QVBoxLayout, QMenu, QSizePolicy)

class Add_Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Add Subject")

        self.menu = QMenu()
        self.menu.setStyleSheet("font-size: 20px;")
        self.menu.aboutToShow.connect(self.update_button)

        self.add_subject()

    def add_subject(self):
        menu_create = self.menu.addAction("Create")
        example_1 = self.menu.addAction("Example 1")
        example_2 = self.menu.addAction("Example 2")
        self.setMenu(self.menu)

    def update_button(self):
        self.menu.setMinimumWidth(self.width())
        