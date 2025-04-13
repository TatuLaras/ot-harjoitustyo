from typing import List
from PyQt6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QPushButton,
)


class StringListManager(QGroupBox):
    """
    A general UI component for managing a list of strings. To use this properly,
    three methods need to be overridden:
    `def get_updated_list(self) -> List[str]`
    `def open_add_dialog(self)`
    `def delete_string(self, string: str)`
    """

    def __init__(
        self,
        title="List",
        add_button_text="Add",
        delete_button_text="Delete",
    ):
        super().__init__()
        self.strings = []

        self.setTitle(title)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()

        buttons = QHBoxLayout()
        button_group_widget = QWidget()
        button_group_widget.setLayout(buttons)

        delete_button_widget = QPushButton(delete_button_text)
        delete_button_widget.clicked.connect(self._delete_currently_selected_string)
        buttons.addWidget(delete_button_widget)

        add_string_button_widget = QPushButton(add_button_text)
        add_string_button_widget.clicked.connect(self.open_add_dialog)
        buttons.addWidget(add_string_button_widget)

        layout.addWidget(self.list_widget)
        layout.addWidget(button_group_widget)

        self.setLayout(layout)

        self.refresh_list()

    def refresh_list(self):
        self.strings = self.get_updated_list()

        # Populate list widget
        self.list_widget.clear()
        for string in self.strings:
            self.list_widget.addItem(string)

    def _delete_currently_selected_string(self):
        """
        Calls the `on_string_delete_requested` callback with the currently selected string.
        """
        selected_index = self.list_widget.currentRow()
        # Nothing selected
        if selected_index < 0:
            return

        self.delete_string(self.strings[selected_index])
        self.refresh_list()

    def get_updated_list(self) -> List[str]:
        return []

    def open_add_dialog(self):
        pass

    def delete_string(self, string: str):
        pass
