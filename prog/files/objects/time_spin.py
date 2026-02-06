from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt, pyqtSignal
from .signal_values import reset_val

class Minutes(QSpinBox):
    min_value = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.initUI()
        self.get_min()
        self.style()

    def initUI(self):
        self.setSingleStep(5)
        self.setMaximum(55)

        self.setWrapping(True)
        self.valueChanged.connect(self.get_min)

        reset_val.value.connect(self.reset_val)
        
        self.setAlignment(Qt.AlignCenter)
        self.setSuffix(" m")

    def reset_val(self):
        self.setValue(0)

    def style(self):
        self.setStyleSheet("""
            QSpinBox{
                    min-height: 50px;
                    font-size: 25px;
                    font-weight: bold;
                    background-color: hsl(209, 87%, 86%);
                    color: hsl(209, 87%, 68%);
                    border-radius: 10px;
                    border: 2px inset hsl(209, 48%, 77%);
                }
                           
            QSpinBox::up-button, QSpinBox::down-button {
                    width: 0px; 
                }
        """)

    def get_min(self):
        minutes_value = self.value()
        self.min_value.emit(minutes_value)



class Hours(QSpinBox):
    h_value = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.initUI()
        self.get_h()
        self.style()

    def initUI(self):
        self.setMaximum(23)

        self.setWrapping(True)
        self.valueChanged.connect(self.h_value.emit)
        self.valueChanged.connect(self.get_h)

        reset_val.value.connect(self.reset_val)


        self.setAlignment(Qt.AlignCenter)
        self.setSuffix(" h")

    def reset_val(self):
        self.setValue(0)

    def style(self):
        self.setStyleSheet("""
            QSpinBox{
                    min-height: 50px;
                    font-size: 25px;
                    font-weight: bold;
                    color: hsl(209, 87%, 68%);
                    background-color: hsl(209, 87%, 86%);
                    border-radius: 10px;
                    border: 2px inset hsl(209, 48%, 79%);
                }
                           
            QSpinBox::up-button, QSpinBox::down-button {
                    width: 0px; 
                }
        """)

    def get_h(self):
        hours_value = self.value()
        self.h_value.emit(hours_value)