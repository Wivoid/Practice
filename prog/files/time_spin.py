from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt

class Minutes(QSpinBox):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setSingleStep(5)
        self.setMaximum(55)

        self.setWrapping(True)

        self.setStyleSheet("""
            QSpinBox{
                    min-height: 50px;
                    font-size: 20px;
                }
                           
            QSpinBox::up-button, QSpinBox::down-button {
                    width: 0px; 
                }
                               
                           """)
        
        self.setAlignment(Qt.AlignCenter)
        self.setSuffix(" m")



class Hours(QSpinBox):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMaximum(23)
        self.setWrapping(True)

        self.setStyleSheet("""
            
            QSpinBox{
                    min-height: 50px;
                    font-size: 20px;
                }
                           
            QSpinBox::up-button, QSpinBox::down-button {
                    width: 0px; 
                }
                               
                           """)
        self.setAlignment(Qt.AlignCenter)
        self.setSuffix(" h")

