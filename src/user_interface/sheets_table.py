import typing
from PyQt6.QtCore import QItemSelection, QSortFilterProxyModel
from PyQt6.QtWidgets import QAbstractItemView, QTableView, QWidget

from entities.sheet import Sheet
from repositories.sheet_repository import SheetRepository
from services.sheet_service import SheetService
from user_interface.model.sheet_model import SheetModel


class SheetsTable(QTableView):
    def __init__(
        self,
        on_sheet_selected: typing.Callable[[Sheet, typing.Callable[[], None]], None],
        parent: typing.Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.sheet_repository = SheetRepository()
        self.sheet_service = SheetService()

        self.sheet_model = SheetModel()
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.sheet_model)
        self.on_sheet_selected = on_sheet_selected

        self.setModel(self.proxy_model)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setSortingEnabled(True)
        self.selectionModel().selectionChanged.connect(self._selection_changed)
        self.setColumnHidden(0, True)

        self.refresh()

    def _selection_changed(self, item: QItemSelection):
        row = item.takeFirst().top()
        sheet_id = self.proxy_model.data(self.proxy_model.index(row, 0))
        self.on_sheet_selected(self.sheet_repository.get(sheet_id), self.sheet_model.updateSheets)

    def refresh(self):
        self.sheet_service.scan_for_sheets()
        self.sheet_model.updateSheets()
