from sqlite3 import Row
from typing import List
from entities.base_entity import BaseEntity
from sql_search_params import SearchParameter
from utils import safe_cast_to_int


class Sheet(BaseEntity):
    """
    Models a single music sheet / piece, corresponding to the database table `sheet`.
    """

    def __init__(self) -> None:
        super().__init__()
        self.sheet_id: int | None = None
        self.file_path: str | None = None
        self.title: str | None = None
        self.composer: str | None = None
        self.genre: str | None = None
        self.difficulty: int | None = None
        self.instrument: str | None = None

    @classmethod
    def from_filepath(cls, file_path: str):
        """
        Constructs an empty Sheet with the file_path property set to `file_path`.
        """
        sheet = Sheet()
        sheet.file_path = file_path
        sheet.title = ""
        return sheet

    @classmethod
    def from_row(cls, row: Row):
        """
        A constructor to make a Sheet from a sqlite `row`.
        """
        sheet = Sheet()
        sheet.sheet_id = row["sheet_id"]
        sheet.instrument = row["instrument"]
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
        """
        Filters out empty strings and ensures correct parameter value types for `search_parameters`.
        """
        valid = []
        for param in search_parameters:
            if isinstance(param.value, str) and len(param.value) == 0:
                continue

            if param.column in ("sheet_id", "difficulty"):
                param.value = safe_cast_to_int(param.value)

            valid.append(param)

        return valid
