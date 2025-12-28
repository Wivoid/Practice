import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QDoubleSpinBox)
from .files.menu_buttons import Add_Button
from .files.time_spin import Hours, Minutes

class Scene2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.middle_layout = QHBoxLayout()

        self.Time_Box()
        self.Recent_Box()
        self.Stats_Box()
        
        self.time()
        
        self.vbox.insertLayout(1, self.middle_layout)

    def Time_Box(self):
        self.time_box = QWidget()
        

        self.time_text = QLabel("00:00", self)
        self.time_text.setAlignment(Qt.AlignCenter)

        self.time_layout = QVBoxLayout(self.time_box)
        self.time_layout.addWidget(self.time_text)

        self.vbox.insertWidget(0, self.time_box)


        self.time_text.setStyleSheet("font: 30px;")

        self.time_box.setObjectName("TimerFrame")
        self.time_box.setFixedHeight(50)

    def Recent_Box(self):
        self.recent_box = QWidget()
        self.recent_info = QWidget()


        self.recent_text = QLabel("Recent Activity", self)
        self.recent_text.setAlignment(Qt.AlignHCenter)

        self.recent_layout = QVBoxLayout(self.recent_box)
        self.recent_layout.addWidget(self.recent_text, stretch=0)
        self.recent_layout.addWidget(self.recent_info, stretch=1)


        self.recent_text.setStyleSheet("font: 30px;")
        self.recent_box.setObjectName("RecentFrame")
        self.recent_info.setStyleSheet("border: 2px solid purple;"
                                       "border-radius: 3px;")

        self.middle_layout.addWidget(self.recent_box)

    def Stats_Box(self):
        self.stats_box = QWidget()
        self.stats_info = QWidget()

        self.stats_text = QLabel("Statistics", self)
        self.stats_text.setAlignment(Qt.AlignCenter)

        self.stats_layout = QVBoxLayout(self.stats_box)
        self.stats_layout.addWidget(self.stats_text, stretch=0)
        self.stats_layout.addWidget(self.stats_info, stretch=1)

        
        self.stats_text.setStyleSheet("font: 30px;")
        self.stats_box.setObjectName("StatsFrame")
        self.stats_info.setStyleSheet("border: 2px solid brown;"
                                       "border-radius: 3px;")

        self.middle_layout.addWidget(self.stats_box)

    def initUI(self):

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout(self)

        self.setLayout(self.vbox)

        self.return_button = QPushButton("Return", self)
        self.add_button = Add_Button()
        self.h_time = Hours()
        self.min_time = Minutes()
        self.focus_button = QPushButton("Focus", self)


        self.hbox.addWidget(self.return_button, stretch=3)
        self.hbox.addWidget(self.add_button, stretch=3)

        self.hbox.addSpacing(15)
        self.hbox.addWidget(self.h_time, stretch=1)
        self.hbox.addSpacing(5)
        self.hbox.addWidget(self.min_time, stretch=1)
        self.hbox.addSpacing(15)

        self.hbox.addWidget(self.focus_button, stretch=3)

        self.vbox.addLayout(self.hbox)


        self.setStyleSheet("""
            QPushButton {
                    font-size: 40px;
                        }
            #TimerFrame {
                border: 2px solid red;
                border-radius: 3px;
                    }
            #RecentFrame {
                border: 2px solid yellow;
                border-radius: 3px;
                        }
            #StatsFrame {
                border: 2px solid green;
                border-radius: 3px;
                        }
        """)

    def time(self):
        self.Time_set = QDateTime()
        self.Timer_upd = QTimer()

        self.visible = True

        self.Timer_upd.start(800)
        self.Timer_upd.timeout.connect(self.update_time)
        
    def update_time(self):
        if self.visible:
            current_date = QDateTime.currentDateTime().toString("dd.MM   HH:mm")
        else:
            current_date = QDateTime.currentDateTime().toString("dd.MM   HH mm")
            
        self.time_text.setText(current_date)
        self.visible = not self.visible

from .files.subj_value import Val
from PyQt5.QtCore import QTimer, QDateTime

class Scene3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Manager - Focus")
        self.initUI()
        self.time()
        

    def initUI(self):
        self.line_box = QWidget()
        self.line_vbox = QVBoxLayout(self.line_box)

        self.vmain_layout = QVBoxLayout()
        self.hlayout = QHBoxLayout()

        stop_btn = QPushButton("Stop")
        pause_btn = QPushButton("Pause")

        self.date_time = QLabel("12:00")
        self.subj_name = QLabel("subject")
        self.subj_timer = QLabel("00:00")

        self.line_vbox.addWidget(self.date_time)
        self.date_time.setAlignment(Qt.AlignCenter)

        
        Val.value.connect(self.timer_name)


        self.setLayout(self.vmain_layout)
        self.hlayout.setContentsMargins(30,0,30,0)

        self.vmain_layout.addWidget(self.line_box)
        self.vmain_layout.addStretch(1)

        self.vmain_layout.addWidget(self.subj_timer)
        self.subj_timer.setAlignment(Qt.AlignCenter)


        self.vmain_layout.addStretch(4)


        self.vmain_layout.addWidget(self.subj_name)
        self.subj_name.setAlignment(Qt.AlignCenter)

        self.vmain_layout.addStretch(2)

        self.vmain_layout.addLayout(self.hlayout)

        self.vmain_layout.addStretch(2)


        stop_btn.setMinimumHeight(120)
        self.hlayout.addWidget(stop_btn)

        pause_btn.setMinimumHeight(120)
        self.hlayout.addWidget(pause_btn)


        self.subj_timer.setObjectName("Subj_Time")
        self.line_box.setObjectName("Frame")
        self.line_box.setFixedHeight(50)

        self.setStyleSheet("""
                #Frame {
                    border: 2px solid red;
                }
                           
                QLabel {
                    font: 30px;
                }
                           
                QPushButton {
                    font-size: 35px;
                    margin: 30px;
                }
                           
                #Subj_Time {
                    font-size: 70px;
                }
        """)

    def timer_name(self, name):
        self.subj_name.setText(name)

    def time(self):
        self.Time_set = QDateTime()
        self.Timer_upd = QTimer()

        self.visible = True

        self.Timer_upd.start(800)
        self.Timer_upd.timeout.connect(self.update_time)
        
    def update_time(self):
        if self.visible:
            current_date = QDateTime.currentDateTime().toString("dd.MM   HH:mm")
        else:
            current_date = QDateTime.currentDateTime().toString("dd.MM   HH mm")
            
        self.date_time.setText(current_date)
        self.visible = not self.visible