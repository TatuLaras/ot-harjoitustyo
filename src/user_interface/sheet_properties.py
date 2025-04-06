import typing
import pprint
from PyQt6.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from entities.sheet import Sheet
from repositories.sheet_repository import SheetRepository
from utils import flatten
from definitions import difficulties


class SheetProperties(QGroupBox):
    def __init__(self, parent: typing.Optional[QWidget] = None):
        super().__init__(parent)
        self.sheet_repository = SheetRepository()
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
        layout.addRow(QLabel("Title"), self.input_title)

        self.input_composer = QLineEdit()
        layout.addRow(QLabel("Composer"), self.input_composer)

        self.input_genre = QLineEdit()
        layout.addRow(QLabel("Genre"), self.input_genre)

        self.input_difficulty = QComboBox()
        for difficulty in difficulties:
            self.input_difficulty.addItem(difficulty)
        layout.addRow(QLabel("Difficulty"), self.input_difficulty)

        # instrument_id

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

        return has_changes

    def set_sheet(self, sheet: Sheet, on_refresh_needed: typing.Callable[[], None]):
        if self.current_sheet is not None:
            refresh_needed = self._update_current_sheet()

            self.sheet_repository.update(self.current_sheet)

            if refresh_needed:
                on_refresh_needed()

        self.input_title.setText(sheet.title)
        self.input_composer.setText(sheet.composer)
        self.input_genre.setText(sheet.genre)
        self.input_difficulty.setCurrentIndex(sheet.difficulty or -1)
        self.current_sheet = sheet
