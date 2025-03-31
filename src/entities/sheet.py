from sqlite3 import Row
from entities.base_entity import BaseEntity


class Sheet(BaseEntity):
    def __init__(self, instrument_id, file_path, title, composer) -> None:
        super().__init__()
        self.instrument_id = instrument_id
        self.file_path = file_path
        self.title = title
        self.composer = composer

    @classmethod
    def from_row(cls, row: Row):
        return cls(
            instrument_id=row["instrument_id"],
            file_path=row["file_path"],
            title=row["title"],
            composer=row["composer"],
        )
