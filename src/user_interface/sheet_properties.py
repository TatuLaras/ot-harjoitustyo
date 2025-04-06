import typing
import pprint
from PyQt6.QtWidgets import (
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
            print(self.current_sheet.title)
            has_changes = True

        if flatten(self.current_sheet.composer) != self.input_composer.text():
            self.current_sheet.composer = self.input_composer.text()
            print(self.current_sheet.composer)
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
        self.current_sheet = sheet
