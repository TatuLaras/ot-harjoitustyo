from PyQt6.QtWidgets import QMenuBar
from user_interface.preference_window.preference_window import PreferenceWindow


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.pref = None

        edit = self.addMenu("Edit")
        action = edit.addAction("Preferences")
        action.triggered.connect(self._open_preferences)

    def _open_preferences(self):
        if self.pref is None:
            self.pref = PreferenceWindow()
        self.pref.show()
