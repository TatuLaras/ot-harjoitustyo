from enum import Enum
from typing import List


class Constraint(Enum):
    EQUIVALENT = 0
    LESS = 1
    LESS_EQUAL = 2
    GREATER = 3
    GREATER_EQUAL = 4
    CONTAINS = 5


class SearchParameter:
    def __init__(self, column: str, value, constraint=Constraint.EQUIVALENT):
        self.column = column
        self.value = value
        self.constraint = constraint

    def to_sql(self):
        """
        Turns the `SearchParameter` into a SQL WHERE-query constraint like "column = 'value'".
        """
        value = f"%{self.value}%" if self.constraint == Constraint.CONTAINS else self.value
        return f"`{self.column}` {self.equivalence_operator} '{value}'"

    @property
    def equivalence_operator(self):
        match self.constraint:
            case Constraint.EQUIVALENT:
                return "="
            case Constraint.LESS:
                return "<"
            case Constraint.LESS_EQUAL:
                return "<="
            case Constraint.GREATER:
                return ">"
            case Constraint.GREATER_EQUAL:
                return ">="
            case Constraint.CONTAINS:
                return "LIKE"


def generate_where_query(params: List[SearchParameter]):
    if len(params) == 0:
        return "1=1"

    return_str = ""

    for i, param in enumerate(params):
        if i > 0:
            return_str += " AND "
        return_str += param.to_sql()

    return return_str
