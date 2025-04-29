from collections.abc import Callable
from typing import List
from PyQt6.QtWidgets import (
    QGroupBox,
    QLayout,
    QPushButton,
    QInputDialog,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QComboBox,
)
from PyQt6.sip import delete
from entities.sheet import Sheet
from entities.search_parameter import SearchParameter
from user_interface.parameter_line import ParameterLine
from services.sheet_service import SheetService


def clear_layout(layout: QLayout):
    while True:
        child = layout.takeAt(0)
        if child is None:
            break

        if child.widget() is not None:
            delete(child.widget())

        delete(child)


class SearchParameterEditor(QGroupBox):
    def __init__(
        self,
        on_params_changed: Callable[[List[SearchParameter]], None],
    ):
        super().__init__()
        self.sheet_service = SheetService()

        self.collection_name_dialog = None

        self.on_params_changed = on_params_changed
        self.params: List[SearchParameter] = []

        self.setTitle("Search parameters")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.collection_select = QComboBox()
        self._update_collections()

        layout.addWidget(self.collection_select)

        params_list_container_widget = QWidget()
        self.params_list_container_layout = QVBoxLayout()
        params_list_container_widget.setLayout(self.params_list_container_layout)
        self.params_list_container_layout.setContentsMargins(0, 0, 0, 0)
        self.params_list_container_layout.setSpacing(0)

        layout.addWidget(params_list_container_widget)

        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout()
        buttons_widget.setLayout(buttons_layout)
        layout.addWidget(buttons_widget)

        save_button_widget = QPushButton("Save collection")
        save_button_widget.clicked.connect(self._open_save_collection_dialog)
        buttons_layout.addWidget(save_button_widget)

        add_button_widget = QPushButton("Add parameter")
        add_button_widget.clicked.connect(self._new_param)
        buttons_layout.addWidget(add_button_widget)

    def _new_param(self):
        self.params.append(SearchParameter(Sheet.columns()[0], 0))
        self._update_params_list()

    def _save_params(self, name: str):
        if len(name) == 0:
            return
        self.sheet_service.create_collection_with_params(
            name,
            self.params,
        )
        self._update_collections()

    def _update_params_list(self):
        self.on_params_changed(self.params)
        clear_layout(self.params_list_container_layout)

        for param in self.params:
            self.params_list_container_layout.addWidget(
                ParameterLine(
                    param, self._delete_param, lambda: self.on_params_changed(self.params)
                )
            )

    def _delete_param(self, search_param: SearchParameter):
        self.params.remove(search_param)
        self._update_params_list()

    def _open_save_collection_dialog(self):
        """
        Opens an input dialog to enter instrument name.
        """
        if self.collection_name_dialog is None:
            self.collection_name_dialog = QInputDialog()
            self.collection_name_dialog.setLabelText("Collection name")
            self.collection_name_dialog.textValueSelected.connect(self._save_params)

        self.collection_name_dialog.show()

    def _collection_selected(self, name: str):
        if len(name) == 0:
            return

        collection_id = self.sheet_service.get_collection_id_by_name(name)
        if collection_id is None:
            return

        self.params = self.sheet_service.get_collection_params(collection_id)
        self._update_params_list()

    def _update_collections(self):
        self.collection_select.clear()
        for collection in self.sheet_service.get_collection_names():
            self.collection_select.addItem(collection)
        self.collection_select.setCurrentIndex(-1)
        self.collection_select.currentTextChanged.connect(self._collection_selected)
