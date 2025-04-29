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
        """
        Gets all sheet directories.
        """
        rows = self.trivial_select("sheet_directory", SheetDirectory.columns())
        return [SheetDirectory.from_row(row) for row in rows]

    def get_instruments(self) -> List[Instrument]:
        """
        Gets all instruments.
        """
        rows = self.trivial_select("instrument", Instrument.columns())
        return [Instrument.from_row(row) for row in rows]

    def create_sheet_directory(self, path: str):
        """
        Creates a sheet directory with `path`.
        """
        self.trivial_insert("sheet_directory", {"path": path})

    def create_instrument(self, name: str):
        """
        Creates a instrument with `name`.
        """
        self.trivial_insert("instrument", {"name": name})

    def delete_sheet_directory(self, path: str):
        """
        Deletes the sheet directory with path `path`.
        """
        self.trivial_delete("sheet_directory", "path", path)

    def delete_instrument(self, name: str):
        """
        Deletes the sheet directory with name `name`.
        """
        self.trivial_delete("instrument", "name", name)
