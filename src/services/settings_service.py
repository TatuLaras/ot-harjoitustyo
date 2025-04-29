from typing import List
from entities.instrument import Instrument
from entities.sheet_directory import SheetDirectory
from repositories.settings_repository import SettingsRepository


class SettingsService:
    """
    Responsible for the logic of the preferences menu.
    """

    def __init__(self, settings_repository=SettingsRepository()) -> None:
        self.settings_repository = settings_repository

    def get_sheet_directories(self) -> List[SheetDirectory]:
        """
        Wrapper for `SettingsRepository.get_sheet_directories`.
        """
        return self.settings_repository.get_sheet_directories()

    def get_instruments(self) -> List[Instrument]:
        """
        Wrapper for `SettingsRepository.get_instruments`.
        """
        return self.settings_repository.get_instruments()

    def create_sheet_directory(self, path: str):
        """
        Wrapper for `SettingsRepository.create_sheet_directory`.
        """
        self.settings_repository.create_sheet_directory(path)

    def create_instrument(self, name: str):
        """
        Wrapper for `SettingsRepository.create_instrument`.
        """
        self.settings_repository.create_instrument(name)

    def delete_sheet_directory(self, path: str):
        """
        Wrapper for `SettingsRepository.delete_sheet_directory`.
        """
        self.settings_repository.delete_sheet_directory(path)

    def delete_instrument(self, name: str):
        """
        Wrapper for `SettingsRepository.delete_instrument`.
        """
        self.settings_repository.delete_instrument(name)
