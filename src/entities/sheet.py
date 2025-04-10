from sqlite3 import Row
from typing import List
from entities.base_entity import BaseEntity
from sql_search_params import Constraint, SearchParameter
from utils import safe_cast_to_int


class Sheet(BaseEntity):
    def __init__(self) -> None:
        super().__init__()
        self.sheet_id: int | None = None
        self.instrument_id: int | None = None
        self.file_path: str | None = None
        self.title: str | None = None
        self.composer: str | None = None
        self.genre: str | None = None
        self.difficulty: int | None = None

    @classmethod
    def from_filepath(cls, file_path: str):
        sheet = Sheet()
        sheet.file_path = file_path
        sheet.title = ""
        return sheet

    @classmethod
    def from_row(cls, row: Row):
        sheet = Sheet()
        sheet.sheet_id = row["sheet_id"]
        sheet.instrument_id = row["instrument_id"]
        sheet.file_path = row["file_path"]
        sheet.title = row["title"]
        sheet.composer = row["composer"]
        sheet.genre = row["genre"]
        sheet.difficulty = row["difficulty"]
        return sheet

    @classmethod
    def sanitize_search_parameters(
        cls,
        search_parameters: List[SearchParameter],
    ) -> List[SearchParameter]:
        valid = []
        for param in search_parameters:
            if isinstance(param.value, str) and len(param.value) == 0:
                continue

            if param.column in ("sheet_id", "instrument_id", "difficulty"):
                param.value = safe_cast_to_int(param.value)

            valid.append(param)

        return valid
