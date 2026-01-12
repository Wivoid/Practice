from PyQt5.QtCore import QObject, pyqtSignal

class Subj_Values(QObject):
    value = pyqtSignal(str)

class Reset_Time(QObject):
    value = pyqtSignal(bool)

reset_val = Reset_Time()
subject_val = Subj_Values()