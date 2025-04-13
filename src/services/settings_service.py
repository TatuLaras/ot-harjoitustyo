from typing import List
from entities.instrument import Instrument
from entities.sheet_directory import SheetDirectory
from repositories.settings_repository import SettingsRepository


class SettingsService:
    def __init__(self, settings_repository=SettingsRepository()) -> None:
        self.settings_repository = settings_repository

    def get_sheet_directories(self) -> List[SheetDirectory]:
        return self.settings_repository.get_sheet_directories()

    def get_instruments(self) -> List[Instrument]:
        return self.settings_repository.get_instruments()

    def create_sheet_directory(self, path: str):
        self.settings_repository.create_sheet_directory(path)

    def create_instrument(self, name: str):
        self.settings_repository.create_instrument(name)

    def delete_sheet_directory(self, path: str):
        self.settings_repository.delete_sheet_directory(path)

    def delete_instrument(self, name: str):
        self.settings_repository.delete_instrument(name)
