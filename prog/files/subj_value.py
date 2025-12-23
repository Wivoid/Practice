from PyQt5.QtCore import QObject, pyqtSignal

class Values(QObject):
    value = pyqtSignal(str)

Val = Values()