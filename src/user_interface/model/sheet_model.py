from typing import Any, List, Optional
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt
from repositories.sheet_repository import SheetRepository
from definitions import difficulties
from services.sheet_service import SheetService
from sql_search_params import SearchParameter


class SheetModel(QAbstractTableModel):
    """
    A subclass of QAbstractTableModel used by the QTableView widget in
    order to have access to the sheet data
    """

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.sheet_service = SheetService()
        self.sheets = []
        self.columns = [
            ("", "sheet_id"),
            ("Title", "title"),
            ("File path", "file_path"),
            ("Composer", "composer"),
            ("Instrument ID", "instrument_id"),
            ("Genre", "genre"),
            ("Difficulty", "difficulty"),
        ]

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.sheets)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.columns)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return

        sheet = self.sheets[index.row()]
        column = self.columns[index.column()][1]

        if column == "difficulty" and sheet.difficulty is not None:
            return difficulties[sheet.difficulty]

        return sheet.__getattribute__(column)

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole
    ) -> Any:
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return
        return self.columns[section][0]

    def updateSheets(self):
        self.beginResetModel()
        self.sheets = self.sheet_service.get_all_sheets()
        self.endResetModel()

    def updateSheetsWithParameters(self, search_parameters: List[SearchParameter]):
        self.beginResetModel()
        self.sheets = self.sheet_service.get_all_sheets_with_params(search_parameters)
        self.endResetModel()
