import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QStackedWidget)
from prog.main_scene import Scene1
from prog.info import Info
from prog.scenes import Scene2
from prog.scenes import Scene3
from prog.files.objects.signal_values import subject_val

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager")
        self.setGeometry(800,500,800,500)
        self.setMinimumSize(850,400)
        self.initUI()
        self.style()

        self.current_subj = ""

    def initUI(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_scene = Scene1()
        self.info_scene = Info()

        self.menu_scene = Scene2()
        self.focus_scene = Scene3()

        self.stack.addWidget(self.main_scene)
        self.stack.addWidget(self.info_scene)
        self.stack.addWidget(self.menu_scene)
        self.stack.addWidget(self.focus_scene)

        
        self.stack.setCurrentIndex(0)


        self.main_scene.start_button.clicked.connect(self.Menu)
        self.main_scene.info_button.clicked.connect(self.Info)
        self.info_scene.return_btn.clicked.connect(self.Info_Return)

        self.menu_scene.return_button.clicked.connect(self.Return_Main)
        self.menu_scene.focus_button.clicked.connect(self.Focus)

        self.focus_scene.end_session.connect(self.End_focus)
        subject_val.value.connect(self.save_subj)

    def Menu(self):
        self.stack.setCurrentIndex(2)

    def Info(self):
        self.stack.setCurrentIndex(1)

    def Info_Return(self):
        self.stack.setCurrentIndex(0)

    def Return_Main(self):
        self.stack.setCurrentIndex(0)

    def Focus(self):
        self.hours = self.menu_scene.h_time.value()
        self.minutes = self.menu_scene.min_time.value()

        if self.hours == 0 and self.minutes == 0:
            self.Subject_warn = QMessageBox.warning(self, 'Warning!', 'Please set the Time')
        else:
            if self.current_subj == '':
                self.Time_warn = QMessageBox.warning(self, 'Warning!', 'Please select subject')
            else:
                self.stack.setCurrentIndex(3)
            self.focus_scene.set_time(self.hours, self.minutes)
            
        
    def End_focus(self):
        self.stack.setCurrentIndex(0)

    def save_subj(self, name):
        self.current_subj = name


    def style(self):
        self.setStyleSheet("""
            QMessageBox QPushButton {
                font-size: 25px;
                font-weight: bold;
                color: hsl(209, 56%, 70%);
                background-color: hsl(209, 87%, 86%);
                border: 3px outset hsl(209, 25%, 60%);
                border-radius: 14px;
                padding: 3px;
            }
                           
            QMessageBox QLabel{
                font-size: 20px;
                font-weight: bold;
                color: hsl(209, 51%, 52%);
            }

            QMessageBox QPushButton::hover {
                color: hsl(209, 56%, 70%);
                background-color: hsl(209, 87%, 89%);
            }

            QWidget{
                background: hsl(210, 89%, 92%);
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())