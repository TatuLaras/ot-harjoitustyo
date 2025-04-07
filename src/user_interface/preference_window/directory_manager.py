from PyQt6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QPushButton,
    QFileDialog,
)

from services.settings_service import SettingsService


class DirectoryManager(QGroupBox):
    """
    Section of the preferences window in which the user can add and remove
    directories to scan sheet music files from
    """

    def __init__(self):
        super().__init__()
        self.settings_service = SettingsService()

        self.dir_picker = None
        self.directories = []

        self.setTitle("Sheet music directories")

        layout = QVBoxLayout()

        self.dir_list_widget = QListWidget()

        buttons = QHBoxLayout()
        button_group_widget = QWidget()
        button_group_widget.setLayout(buttons)

        delete_button_widget = QPushButton("Delete folder")
        delete_button_widget.clicked.connect(self._delete_current_directory)
        buttons.addWidget(delete_button_widget)

        add_dir_button_widget = QPushButton("Add folder")
        add_dir_button_widget.clicked.connect(self._open_directory_picker)
        buttons.addWidget(add_dir_button_widget)

        layout.addWidget(self.dir_list_widget)
        layout.addWidget(button_group_widget)

        self.setLayout(layout)

        self._update_dir_list()

    def _update_dir_list(self):
        """
        Gets the updated list of directories from the database and populates
        the list widgets along with the internal list
        """
        self.directories = self.settings_service.get_sheet_directories()

        # Populate list widget
        self.dir_list_widget.clear()
        for directory in self.directories:
            self.dir_list_widget.addItem(directory.path)

    def _delete_current_directory(self):
        """
        Deletes the directory which is currently selected in the list widget
        """
        selected_index = self.dir_list_widget.currentRow()
        # Nothing selected
        if selected_index < 0:
            return

        self.settings_service.delete_sheet_directory(
            self.directories[selected_index].sheet_directory_id
        )
        self._update_dir_list()

    def _directory_picker_file_selected(self, path: str | None):
        """
        Called whenever a directory is selected in the directory picker
        """
        if path is None:
            return

        self.settings_service.create_sheet_directory(path)
        self._update_dir_list()

    def _open_directory_picker(self):
        """
        Opens a directory picker window
        """
        if self.dir_picker is None:
            self.dir_picker = QFileDialog()
            self.dir_picker.setFileMode(QFileDialog.FileMode.Directory)
            self.dir_picker.setOption(QFileDialog.Option.ShowDirsOnly, True)
            self.dir_picker.fileSelected.connect(self._directory_picker_file_selected)

        self.dir_picker.show()
