from typing import List
from entities.sheet import Sheet
from repositories.base_repository import BaseRepository
from sql_query_generators import DuplicateHandling
from sql_search_params import SearchParameter


class SheetRepository(BaseRepository):
    def get(self, sheet_id: int) -> Sheet | None:
        row = self.trivial_id_select("sheet", Sheet.columns(), "sheet_id", sheet_id)
        if row is None:
            return None
        return Sheet.from_row(row)

    def get_all(self) -> List[Sheet]:
        rows = self.trivial_select("sheet", Sheet.columns())
        return [Sheet.from_row(row) for row in rows]

    def get_all_with_params(self, search_parameters: List[SearchParameter]) -> List[Sheet]:
        rows = self.trivial_select_with_params(
            "sheet", Sheet.columns(), Sheet.sanitize_search_parameters(search_parameters)
        )
        return [Sheet.from_row(row) for row in rows]

    def create(self, sheet: Sheet):
        self.trivial_insert("sheet", sheet.to_dict())

    def update(self, sheet: Sheet):
        self.trivial_insert("sheet", sheet.to_dict(), DuplicateHandling.UPDATE)

    def create_many(self, sheets: List[Sheet]):
        self.trivial_insert_many("sheet", [sheet.to_dict() for sheet in sheets])

    def delete(self, sheet_id: int):
        self.trivial_delete("sheet", "sheet_id", sheet_id)
