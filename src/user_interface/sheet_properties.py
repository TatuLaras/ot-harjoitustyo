from collections.abc import Callable
from typing import Optional
from PyQt6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGroupBox,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from entities.sheet import Sheet
from services.settings_service import SettingsService
from services.sheet_service import SheetService
from utils import flatten
from definitions import difficulties


class SheetProperties(QGroupBox):
    """
    A right-hand-side panel for editing properties of the currently selected sheet.
    """

    def __init__(self, on_refresh_needed: Callable[[], None], parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.sheet_service = SheetService()
        self.settings_service = SettingsService()
        self.on_refresh_needed = on_refresh_needed
        self.current_sheet: Sheet | None = None

        self.setTitle("Sheet properties")
        wrapper = QVBoxLayout()
        self.setLayout(wrapper)
        wrapper.addStrut(400)

        widget = QWidget()
        layout = QFormLayout()
        widget.setLayout(layout)
        wrapper.addWidget(widget)

        self.input_title = QLineEdit()
        layout.addRow("Title", self.input_title)

        self.input_composer = QLineEdit()
        layout.addRow("Composer", self.input_composer)

        self.input_genre = QLineEdit()
        layout.addRow("Genre", self.input_genre)

        self.input_difficulty = QComboBox()
        for difficulty in difficulties:
            self.input_difficulty.addItem(difficulty)
        layout.addRow("Difficulty", self.input_difficulty)

        self.input_instrument = QComboBox()
        for instrument in [x.name for x in self.settings_service.get_instruments()]:
            self.input_instrument.addItem(instrument)
        layout.addRow("Instrument", self.input_instrument)

        save_button_widget = QPushButton("Save")
        save_button_widget.clicked.connect(self._save_current_sheet)
        layout.addRow(None, save_button_widget)

    def _update_current_sheet(self) -> bool:
        """
        Updates changes from the form inputs to the `current_sheet` class member.
        Returns true if changes were present.
        """
        if self.current_sheet is None:
            return False

        has_changes = False

        if flatten(self.current_sheet.title) != self.input_title.text():
            self.current_sheet.title = self.input_title.text()
            has_changes = True

        if flatten(self.current_sheet.composer) != self.input_composer.text():
            self.current_sheet.composer = self.input_composer.text()
            has_changes = True

        if flatten(self.current_sheet.genre) != self.input_genre.text():
            self.current_sheet.genre = self.input_genre.text()
            has_changes = True

        if (
            self.input_difficulty.currentIndex() >= 0
            and self.current_sheet.difficulty != self.input_difficulty.currentIndex()
        ):
            self.current_sheet.difficulty = self.input_difficulty.currentIndex()
            has_changes = True

        if (
            self.input_instrument.currentIndex() >= 0
            and self.current_sheet.instrument != self.input_instrument.currentText()
        ):
            self.current_sheet.instrument = self.input_instrument.currentText()
            has_changes = True

        return has_changes

    def set_sheet(self, sheet: Sheet):
        """
        Sets the sheet object to be currently edited, saves previous one if changes were made.
        """
        self._save_current_sheet()

        self.input_title.setText(sheet.title)
        self.input_composer.setText(sheet.composer)
        self.input_genre.setText(sheet.genre)
        self.input_difficulty.setCurrentIndex(sheet.difficulty or -1)

        instruments = [x.name for x in self.settings_service.get_instruments()]
        self.input_instrument.clear()
        for instrument in instruments:
            self.input_instrument.addItem(instrument)

        try:
            self.input_instrument.setCurrentIndex(instruments.index(sheet.instrument))
        except ValueError:
            self.input_instrument.setCurrentIndex(-1)

        self.current_sheet = sheet

    def _save_current_sheet(self):
        if self.current_sheet is None:
            return

        refresh_needed = self._update_current_sheet()

        self.sheet_service.update_sheet(self.current_sheet)

        if refresh_needed:
            self.on_refresh_needed()
