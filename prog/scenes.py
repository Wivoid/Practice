import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy)
from .files.menu_buttons import Add_Button

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
        self.middle_layout.addLayout(self.stats_layout)
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

        self.focus_button = QPushButton("Focus", self)
        self.add_button = Add_Button()
        self.return_button = QPushButton("Return", self)


        self.hbox.addWidget(self.return_button)
        self.hbox.addWidget(self.add_button)
        self.hbox.addWidget(self.focus_button)

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

        self.update_time()
        self.Timer_upd.start(1)
        self.Timer_upd.timeout.connect(self.update_time)
        
    def update_time(self):
        current_date = self.Time_set.currentDateTime().toString("dd.MM   HH:mm")

        self.time_text.setText(current_date)


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

        subj_name = QLabel()


        self.setLayout(self.vmain_layout)
        self.hlayout.setContentsMargins(30,0,30,0)

        self.vmain_layout.addLayout(self.line_vbox)
        self.vmain_layout.addWidget(self.line_box)


        self.vmain_layout.addStretch(3)

        self.vmain_layout.addWidget(subj_name)
        self.vmain_layout.addLayout(self.hlayout)

        self.vmain_layout.addStretch(1)


        stop_btn.setMinimumHeight(120)
        self.hlayout.addWidget(stop_btn)

        pause_btn.setMinimumHeight(120)
        self.hlayout.addWidget(pause_btn)


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
        """)

    def time(self):
        self.Time_set = QDateTime()
        self.Timer_upd = QTimer()

        self.Time = QLabel("00:00", self.line_box)
        self.Time.setAlignment(Qt.AlignCenter)


        self.line_vbox.addWidget(self.Time)

        self.update_time()
        self.Timer_upd.start(1)
        self.Timer_upd.timeout.connect(self.update_time)
        
    def update_time(self):
        current_date = self.Time_set.currentDateTime().toString("dd.MM   HH:mm")
        self.Time.setText(current_date)