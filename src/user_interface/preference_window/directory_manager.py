from PyQt6.QtWidgets import (
    QFileDialog,
)

from services.settings_service import SettingsService
from user_interface.preference_window.string_list_manager import StringListManager


class DirectoryManager(StringListManager):
    """
    Section of the preferences window in which the user can add and remove
    directories to scan sheet music files from
    """

    def __init__(self):
        self.settings_service = SettingsService()
        self.dir_picker = None
        super().__init__(
            title="Sheet music folders",
            add_button_text="Add folder",
            delete_button_text="Delete folder",
        )

    # Overrides

    def get_updated_list(self):
        return [x.path for x in self.settings_service.get_sheet_directories() if x.path is not None]

    def delete_string(self, string: str):
        self.settings_service.delete_sheet_directory(string)

    def open_add_dialog(self):
        """
        Opens a directory picker window
        """
        if self.dir_picker is None:
            self.dir_picker = QFileDialog()
            self.dir_picker.setFileMode(QFileDialog.FileMode.Directory)
            self.dir_picker.setOption(QFileDialog.Option.ShowDirsOnly, True)
            self.dir_picker.fileSelected.connect(self._directory_picker_file_selected)

        self.dir_picker.show()

    # Overrides end

    def _directory_picker_file_selected(self, path: str | None):
        """
        Called whenever a directory is selected in the directory picker
        """
        if path is None:
            return

        self.settings_service.create_sheet_directory(path)
        self.refresh_list()
