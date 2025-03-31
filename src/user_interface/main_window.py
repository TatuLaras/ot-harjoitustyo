from PyQt6.QtWidgets import QListWidget, QMainWindow, QTableWidget, QToolBar
from repositories.sheet_repository import SheetRepository
from services.sheet_service import SheetService
from user_interface.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sheet_repository = SheetRepository()
        self.sheet_service = SheetService()

        self.setMenuBar(MenuBar())
        self.setWindowTitle("Sheet music management program")

        self.sheets_list_widget = QListWidget()
        toolbar = QToolBar()
        refresh_action = toolbar.addAction("Refresh")
        refresh_action.triggered.connect(self._refresh)

        self.addToolBar(toolbar)
        self.setCentralWidget(self.sheets_list_widget)

        self.sheet_service.scan_for_sheets()
        self._update_sheet_table_widget()
        self.show()

    def _refresh(self):
        self.sheet_service.scan_for_sheets()
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
