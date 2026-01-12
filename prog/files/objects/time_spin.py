from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt, pyqtSignal
from .signal_values import reset_val

class Minutes(QSpinBox):
    min_value = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.initUI()
        self.get_min()

    def initUI(self):
        self.setSingleStep(5)
        self.setMaximum(55)

        self.setWrapping(True)
        self.valueChanged.connect(self.get_min)

        reset_val.value.connect(self.reset_val)

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

    def reset_val(self):
        self.setValue(0)

    def get_min(self):
        minutes_value = self.value()
        self.min_value.emit(minutes_value)



class Hours(QSpinBox):
    h_value = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.initUI()
        self.get_h()

    def initUI(self):
        self.setMaximum(23)

        self.setWrapping(True)
        self.valueChanged.connect(self.h_value.emit)
        self.valueChanged.connect(self.get_h)

        reset_val.value.connect(self.reset_val)

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

    def reset_val(self):
        self.setValue(0)

    def get_h(self):
        hours_value = self.value()
        self.h_value.emit(hours_value)