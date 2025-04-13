from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)
from user_interface.preference_window.directory_manager import DirectoryManager
from user_interface.preference_window.instrument_manager import InstrumentManager


class PreferenceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preferences")

        layout = QHBoxLayout()
        self.setLayout(layout)

        directory_manager = DirectoryManager()
        layout.addWidget(directory_manager)

        instrument_manager = InstrumentManager()
        layout.addWidget(instrument_manager)

        return
