from repositories.settings_repository import SettingsRepository
from repositories.sheet_repository import SheetRepository
from directory_scanning import scan_directory_for_sheets


class SheetService:
    def __init__(self) -> None:
        self.settings_repository = SettingsRepository()
        self.sheet_repository = SheetRepository()

    def scan_for_sheets(self):
        """
        Scans all directories for sheet music and inserts them into the
        database. Also refreshes the sheets table widget.
        """
        for sheet_directory in self.settings_repository.get_sheet_directories():
            sheets = scan_directory_for_sheets(sheet_directory.path)
            self.sheet_repository.create_many(sheets)
