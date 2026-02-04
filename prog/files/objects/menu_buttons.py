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

        self.Menu = QMenu()
        self.Menu.setAttribute(Qt.WA_TranslucentBackground)
        self.Menu.setWindowFlags(self.Menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.Menu.aboutToShow.connect(self.update_button)

        self.add_subject()
        self.style()

    def add_subject(self):
        self.menu_create = self.Menu.addAction("Create")
        self.menu_create.triggered.connect(self.add_funct)
        self.setMenu(self.Menu)

    def update_button(self):
        self.Menu.setMinimumWidth(self.width())
        
    def add_funct(self):
        self.new_window = AddWindow()
        self.new_window.show()

        self.new_window.subj_send.connect(self.create_subj)

    def create_subj(self, name):
        self.subj = self.Menu.addAction(name)

        self.subj.triggered.connect(lambda: self.subject_funct(name))

        self.setText(name)
        subject_val.value.emit(name)

    def subject_funct(self, name):
        self.setText(name)
        subject_val.value.emit(name)
        
    def style(self):
        self.Menu.setStyleSheet("""
            QMenu{
                background-color: hsl(210, 89%, 92%);
                border: 3px solid hsl(210, 89%, 80%);
                font-size: 20px;
                font-weight: bold;
                border-radius: 10px;
                color: hsl(209, 56%, 70%);
            }
                                
            QMenu::item{
                background: transparent;
            }
                                
            QMenu::item:selected {
                background-color: hsl(210, 89%, 85%);
                color: hsl(209, 56%, 55%);
            }
        """)

