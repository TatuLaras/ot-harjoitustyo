from collections.abc import Callable
from typing import List
from PyQt6.QtCore import QItemSelection, QSortFilterProxyModel
from PyQt6.QtWidgets import QAbstractItemView, QTableView

from entities.sheet import Sheet
from services.sheet_service import SheetService
from sql_search_params import SearchParameter
from user_interface.model.sheet_model import SheetModel


class SheetsTable(QTableView):
    """
    Displays all stored sheet data in a table view widget
    """

    def __init__(
        self,
        on_sheet_selected: Callable[[Sheet], None] | None = None,
    ) -> None:
        """
        `on_sheet_selected`: Callback for when a sheet is selected on the table view widget
        """
        super().__init__()
        self.sheet_service = SheetService()
        self.current_sheet: Sheet | None = None
        self.params = []

        self.sheet_model = SheetModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.sheet_model)
        self.on_sheet_selected = on_sheet_selected

        self.setModel(self.proxy_model)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSortingEnabled(True)
        self.selectionModel().selectionChanged.connect(self._on_selection_changed)
        self.doubleClicked.connect(self._open_current_sheet)

        self.setColumnHidden(0, True)

        self.refresh()

    def _on_selection_changed(self, item: QItemSelection):
        row = item.takeFirst().top()
        sheet_id = self.proxy_model.data(self.proxy_model.index(row, 0))
        self.current_sheet = self.sheet_service.get_sheet_by_id(sheet_id)

        if self.on_sheet_selected is not None:
            self.on_sheet_selected(self.current_sheet)

    def _open_current_sheet(self):
        if self.current_sheet is not None and self.current_sheet.file_path is not None:
            self.sheet_service.open_file(self.current_sheet.file_path)

    def refresh(self):
        self.sheet_service.scan_for_sheets()
        self.update_sheets_from_db()

    def update_sheets_from_db(self):
        if len(self.params) > 0:
            self.sheet_model.updateSheetsWithParameters(self.params)
        else:
            self.sheet_model.updateSheets()

    def on_params_changed(self, search_params: List[SearchParameter]):
        self.params = search_params
        self.update_sheets_from_db()
