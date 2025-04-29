from collections.abc import Callable
from PyQt6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtWidgets import QWidget

from entities.sheet import Sheet
from entities.search_parameter import Relation, SearchParameter


class ParameterLine(QWidget):
    def __init__(
        self,
        search_param: SearchParameter,
        on_param_remove: Callable[[SearchParameter], None],
        on_params_changed: Callable[[], None],
    ):
        super().__init__()

        def update_column(new_text: str):
            search_param.column = new_text
            on_params_changed()

        def update_relation(new_text: str):
            value = relations.get(new_text)
            if value is not None:
                search_param.relation = value
                on_params_changed()

        def update_value(new_text: str):
            search_param.value = new_text
            on_params_changed()

        relations = Relation.__members__
        columns = Sheet.columns()

        layout = QHBoxLayout()
        self.setLayout(layout)

        # Column select
        column_select = QComboBox()
        for column in columns:
            column_select.addItem(column)
        column_select.setCurrentText(search_param.column)

        column_select.currentTextChanged.connect(update_column)
        layout.addWidget(column_select)

        # Relation select
        relation_select = QComboBox()
        for relation in relations:
            relation_select.addItem(relation)
        relation_select.setCurrentText(search_param.relation.name)

        relation_select.currentTextChanged.connect(update_relation)
        layout.addWidget(relation_select)

        # Value
        value_input = QLineEdit()
        value_input.setText(str(search_param.value))

        value_input.textChanged.connect(update_value)
        layout.addWidget(value_input)

        # Delete button
        delete_button = QPushButton("Delete")

        delete_button.clicked.connect(lambda: on_param_remove(search_param))
        layout.addWidget(delete_button)
