from PyQt6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QToolBar,
    QWidget,
)
from repositories.sheet_repository import SheetRepository
from user_interface.menu_bar import MenuBar
from user_interface.sheet_properties import SheetProperties
from user_interface.sheets_table import SheetsTable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sheet_repository = SheetRepository()

        self.setMenuBar(MenuBar())
        self.setWindowTitle("Sheet music management program")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        sheet_properties = SheetProperties()
        sheets_table_widget = SheetsTable(sheet_properties.set_sheet)

        layout.addWidget(sheets_table_widget)
        layout.addWidget(sheet_properties)

        layout.setStretch(0, 1)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        refresh_action = toolbar.addAction("Refresh")
        refresh_action.triggered.connect(sheets_table_widget.refresh)

        self.show()
