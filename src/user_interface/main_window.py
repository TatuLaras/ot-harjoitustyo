from PyQt6.QtWidgets import QListWidget, QMainWindow, QTableWidget, QToolBar
from directory_scanning import scan_directory_for_sheets
from repositories.settings_repository import SettingsRepository
from repositories.sheet_repository import SheetRepository
from user_interface.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings_repository = SettingsRepository()
        self.sheet_repository = SheetRepository()

        self.setMenuBar(MenuBar())
        self.setWindowTitle("Sheet music management program")

        self.sheets_list_widget = QListWidget()
        toolbar = QToolBar()
        refresh_action = toolbar.addAction("Refresh")
        refresh_action.triggered.connect(self._scan_for_sheets)

        self.addToolBar(toolbar)
        self.setCentralWidget(self.sheets_list_widget)

        self._scan_for_sheets()
        self.show()

    def _scan_for_sheets(self):
        """
        Scans all directories for sheet music and inserts them into the
        database. Also refreshes the sheets table widget.
        """
        for sheet_directory in self.settings_repository.get_sheet_directories():
            sheets = scan_directory_for_sheets(sheet_directory.path)
            self.sheet_repository.create_sheets_many(sheets)

        self._update_sheet_table_widget()

    def _update_sheet_table_widget(self):
        """
        Gets the newest sheets from the database and updates the table widget.
        """
        sheets = self.sheet_repository.get_sheets()

        # Populate list widget
        self.sheets_list_widget.clear()
        for sheet in sheets:
            self.sheets_list_widget.addItem(sheet.title)
