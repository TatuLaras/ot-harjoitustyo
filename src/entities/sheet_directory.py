from sqlite3 import Row
from entities.base_entity import BaseEntity


class SheetDirectory(BaseEntity):
    """
    Models a single user-defined music sheet directory in settings,
    corresponding to the database table sheet_directory.
    """

    def __init__(self):
        super().__init__()
        self.sheet_directory_id: int | None = None
        self.path: str | None = None

    @classmethod
    def from_row(cls, row: Row):
        """
        A constructor to make a SheetDirectory from a sqlite Row `row`.
        """
        sheet_directory = SheetDirectory()
        sheet_directory.sheet_directory_id = row["sheet_directory_id"]
        sheet_directory.path = row["path"]
        return sheet_directory
