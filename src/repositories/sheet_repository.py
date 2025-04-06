from typing import List
from entities.sheet import Sheet
from repositories.base_repository import BaseRepository
from sql_query_generators import DuplicateHandling


class SheetRepository(BaseRepository):
    def get(self, sheet_id: int) -> Sheet:
        row = self.trivial_id_select(
            "sheet",
            ["sheet_id", "instrument_id", "file_path", "title", "composer"],
            "sheet_id",
            sheet_id,
        )
        return Sheet.from_row(row)

    def get_all(self) -> List[Sheet]:
        rows = self.trivial_select(
            "sheet", ["sheet_id", "instrument_id", "file_path", "title", "composer"]
        )
        return [Sheet.from_row(row) for row in rows]

    def create(self, sheet: Sheet):
        self.trivial_insert("sheet", sheet.to_dict())

    def update(self, sheet: Sheet):
        self.trivial_insert("sheet", sheet.to_dict(), DuplicateHandling.Update)

    def create_many(self, sheets: List[Sheet]):
        self.trivial_insert_many("sheet", [sheet.to_dict() for sheet in sheets])

    def delete(self, sheet_id: int):
        self.trivial_delete("sheet", "sheet_id", sheet_id)
