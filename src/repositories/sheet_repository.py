from typing import List
from entities.sheet import Sheet
from repositories.base_repository import BaseRepository


class SheetRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    def get_sheets(self) -> List[Sheet]:
        rows = self.trivial_select(
            "sheet", ["instrument_id", "file_path", "title", "composer"]
        )
        return [Sheet.from_row(row) for row in rows]

    def create_sheet(self, sheet: Sheet):
        self.trivial_insert("sheet", sheet.to_dict())

    def create_sheets_many(self, sheets: List[Sheet]):
        self.trivial_insert_many("sheet", [sheet.to_dict() for sheet in sheets])

    def delete_sheet(self, sheet_id: int):
        self.trivial_delete("sheet", "sheet_id", sheet_id)
