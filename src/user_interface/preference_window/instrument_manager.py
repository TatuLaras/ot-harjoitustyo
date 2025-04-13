from PyQt6.QtWidgets import (
    QInputDialog,
)

from services.settings_service import SettingsService
from user_interface.preference_window.string_list_manager import StringListManager


class InstrumentManager(StringListManager):
    """
    Section of the preferences window in which the user can add and remove
    directories to scan sheet music files from
    """

    def __init__(self):
        self.settings_service = SettingsService()
        self.add_instrument_dialog = None
        super().__init__(
            title="Instruments",
            add_button_text="Add instrument",
            delete_button_text="Delete instrument",
        )

    # Overrides

    def get_updated_list(self):
        return [x.name for x in self.settings_service.get_instruments() if x.name is not None]

    def delete_string(self, string: str):
        self.settings_service.delete_instrument(string)

    def open_add_dialog(self):
        """
        Opens an input dialog to enter instrument name.
        """
        if self.add_instrument_dialog is None:
            self.add_instrument_dialog = QInputDialog()
            self.add_instrument_dialog.setLabelText("Instrument name")
            self.add_instrument_dialog.textValueSelected.connect(self._name_entered_in_dialog)

        self.add_instrument_dialog.show()

    # Overrides end

    def _name_entered_in_dialog(self, name: str | None):
        """
        Called whenever a directory is selected in the directory picker
        """
        if name is None:
            return

        self.settings_service.create_instrument(name)
        self.refresh_list()
