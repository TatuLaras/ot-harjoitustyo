from collections.abc import Callable
from typing import List
from PyQt6.QtWidgets import (
    QGroupBox,
    QLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.sip import delete
from entities.sheet import Sheet
from sql_search_params import SearchParameter
from user_interface.parameter_line import ParameterLine


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
        self.on_params_changed = on_params_changed
        self.params: List[SearchParameter] = []

        self.setTitle("Search parameters")

        layout = QVBoxLayout()
        self.setLayout(layout)

        params_list_container_widget = QWidget()
        self.params_list_container_layout = QVBoxLayout()
        params_list_container_widget.setLayout(self.params_list_container_layout)
        self.params_list_container_layout.setContentsMargins(0, 0, 0, 0)
        self.params_list_container_layout.setSpacing(0)

        layout.addWidget(params_list_container_widget)
        add_param_button_widget = QPushButton("Add")
        add_param_button_widget.clicked.connect(self._new_param)
        layout.addWidget(add_param_button_widget)

    def _new_param(self):
        self.params.append(SearchParameter(Sheet.columns()[0], 0))
        self._update_params_list()

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
