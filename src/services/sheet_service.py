import subprocess
from typing import List
from entities.sheet import Sheet
from repositories.settings_repository import SettingsRepository
from repositories.sheet_repository import SheetRepository
from directory_scanning import scan_directory_for_sheets
from sql_search_params import SearchParameter


class SheetService:
    """
    Responsible for the logic of the main application (that is, not the preferences menu).
    """

    def __init__(
        self, settings_repository=SettingsRepository(), sheet_repository=SheetRepository()
    ) -> None:
        self.settings_repository = settings_repository
        self.sheet_repository = sheet_repository

    def scan_for_sheets(self):
        """
        Scans all directories for sheet music and inserts them into the
        database. Also refreshes the sheets table widget.
        """
        for sheet_directory in self.settings_repository.get_sheet_directories():
            sheets = scan_directory_for_sheets(sheet_directory.path)
            self.sheet_repository.create_many(sheets)

    def open_file(self, file_path: str):
        """
        Opens a file at `file_path` using the users default program for that filetype.
        This is not portable, only works on Linux with xdg-open installed
        (which is most Linux systems).
        """
        subprocess.Popen(["xdg-open", file_path])

    def get_sheet_by_id(self, sheet_id: int) -> Sheet | None:
        """
        Wrapper for `SheetRepository.get`.
        """
        return self.sheet_repository.get(sheet_id)

    def get_all_sheets(self) -> List[Sheet]:
        """
        Wrapper for `SheetRepository.get_all`.
        """
        return self.sheet_repository.get_all()

    def get_all_sheets_with_params(self, search_parameters: List[SearchParameter]) -> List[Sheet]:
        """
        Wrapper for `SheetRepository.get_all_with_params`.
        """
        return self.sheet_repository.get_all_with_params(search_parameters)

    def create_sheet(self, sheet: Sheet):
        """
        Wrapper for `SheetRepository.create`.
        """
        self.sheet_repository.create(sheet)

    def update_sheet(self, sheet: Sheet):
        """
        Wrapper for `SheetRepository.update`.
        """
        self.sheet_repository.update(sheet)

    def create_many_sheets(self, sheets: List[Sheet]):
        """
        Wrapper for `SheetRepository.create_many`.
        """
        self.sheet_repository.create_many(sheets)

    def delete_sheet(self, sheet_id: int):
        """
        Wrapper for `SheetRepository.delete`.
        """
        self.sheet_repository.delete(sheet_id)
