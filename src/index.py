import sys
from PyQt6.QtWidgets import QApplication
from db import init_schema
from repositories.settings_repository import SettingsRepository
from user_interface.main_window import MainWindow


init_schema()

settings_repository = SettingsRepository()

app = QApplication(sys.argv)

main_window = MainWindow()

app.exec()
