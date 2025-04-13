from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QToolBar,
    QWidget,
)
from user_interface.menu_bar import MenuBar
from user_interface.search_parameter_editor import SearchParameterEditor
from user_interface.sheet_properties import SheetProperties
from user_interface.sheets_table import SheetsTable


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMenuBar(MenuBar())
        self.setWindowTitle("Sheet music management program")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QHBoxLayout()
        main_widget.setLayout(layout)

        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)

        sheets_table_widget = SheetsTable()
        sheet_properties = SheetProperties(sheets_table_widget.update_sheets_from_db)
        sheets_table_widget.on_sheet_selected = sheet_properties.set_sheet

        left_layout.addWidget(SearchParameterEditor(sheets_table_widget.on_params_changed))
        left_layout.addWidget(sheets_table_widget)

        layout.addWidget(left_widget)
        layout.addWidget(sheet_properties)

        layout.setStretch(0, 1)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        refresh_action = toolbar.addAction("Refresh")
        refresh_action.triggered.connect(sheets_table_widget.refresh)

        self.show()
