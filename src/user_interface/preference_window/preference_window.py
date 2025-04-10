from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from user_interface.preference_window.directory_manager import DirectoryManager


class PreferenceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preferences")

        layout = QVBoxLayout()
        self.setLayout(layout)

        directory_manager = DirectoryManager()
        layout.addWidget(directory_manager)

        return
