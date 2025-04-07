from typing import List

from entities.sheet_directory import SheetDirectory
from repositories.base_repository import BaseRepository


class SettingsRepository(BaseRepository):
    """
    Tied to several small tables, handles things set from the preferences
    window (`PreferencesWindow`)
    """

    def get_sheet_directories(self) -> List[SheetDirectory]:
        rows = self.trivial_select("sheet_directory", SheetDirectory.columns())
        return [SheetDirectory.from_row(row) for row in rows]

    def create_sheet_directory(self, path: str):
        self.trivial_insert("sheet_directory", {"path": path})

    def delete_sheet_directory(self, sheet_id: int):
        self.trivial_delete("sheet_directory", "sheet_directory_id", sheet_id)
