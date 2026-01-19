# ⏱️ Time Manager (v1.0.0)

**Time Manager** is a desktop productivity application built in order to mastership ***PyQt5 Framework***
  
**It is designed** with *passion* to help users manage their work sessions with fulfilment through the clean scene-based interface.

---

## 🚀 Key Features

* **Multi-Scene Interface:** Smooth transitions between the Welcome screen, Dashboard, and Focus mode using `QStackedWidget`.
* **Dynamic Subject Management:** Create and select custom tasks via an interactive menu system.
* **Precise Session Configuration:** Custom-styled `QSpinBox` widgets for setting focus duration (hours and minutes).
* **Live Countdown Timer:** A real-time engine powered by `QTimer` with dynamic UI updates
* **Audio Notifications:** Automatic MP3 sound alerts upon session completion using `QMediaPlayer`.

---

## 🛠 Tech Stack

* **Language:** Python 3.10+
* **GUI Framework:** PyQt5 
* **Architecture:** Separated logic for scenes, custom UI objects, and main window controller.
    * **Signal-Slot Communication:** Decoupled component interaction using `pyqtSignal`



---

## 📂 Project Structure

```text
├── Time_Manager.py      # Main Application file
├── scenes.py            # Core program layouts
├── add_window.py        # Task creation interface
└── files/
    ├── media/           # Media assets 
    └── objects/         # UI components 
