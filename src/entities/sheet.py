from sqlite3 import Row
from entities.base_entity import BaseEntity


class Sheet(BaseEntity):
    def __init__(self) -> None:
        super().__init__()
        self.sheet_id: None | str = None
        self.instrument_id: None | str = None
        self.file_path: None | str = None
        self.title: None | str = None
        self.composer: None | str = None

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
        return sheet
