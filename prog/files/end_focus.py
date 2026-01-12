from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
import sys

class Confirmation(QWidget):
    result = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmation Window")
        self.setFixedSize(500,250)

        self.initUI()
        self.Style()

    def initUI(self):
        print(21111)
        self.question = QLabel("Are you sure?")
        self.yes = QPushButton("Yes")
        self.no = QPushButton("No")

        self.question.setAlignment(Qt.AlignCenter)

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.vbox.addStretch(3)

        self.setLayout(self.vbox)
        self.vbox.addWidget(self.question)

        self.vbox.addStretch(3)
        self.vbox.addLayout(self.hbox)

        self.hbox.addWidget(self.yes)
        self.hbox.addWidget(self.no)

        self.vbox.addStretch(3)


        self.yes.clicked.connect(self.Yes)
        self.no.clicked.connect(self.No)
    
    def Style(self):
        self.setStyleSheet("""
                QLabel{
                    font-size: 60px;
                }
                
                QPushButton{
                    font-size: 40px;
                }
        """)

    def Yes(self):
        self.result.emit(True)
        self.close()

    def No(self):
        self.result.emit(False)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Confirmation()
    window.show()
    sys.exit(app.exec_())