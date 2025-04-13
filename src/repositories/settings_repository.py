from typing import List

from entities.instrument import Instrument
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

    def get_instruments(self) -> List[Instrument]:
        rows = self.trivial_select("instrument", Instrument.columns())
        return [Instrument.from_row(row) for row in rows]

    def create_sheet_directory(self, path: str):
        self.trivial_insert("sheet_directory", {"path": path})

    def create_instrument(self, name: str):
        self.trivial_insert("instrument", {"name": name})

    def delete_sheet_directory(self, path: str):
        self.trivial_delete("sheet_directory", "path", path)

    def delete_instrument(self, name: str):
        self.trivial_delete("instrument", "name", name)
