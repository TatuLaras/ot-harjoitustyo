from sqlite3 import Row
from entities.base_entity import BaseEntity


class SheetDirectory(BaseEntity):
    def __init__(self, row: Row) -> None:
        super().__init__()

        self.sheet_directory_id = row["sheet_directory_id"]
        self.path = row["path"]
