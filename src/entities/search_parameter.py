from sqlite3 import Row
from enum import Enum
from entities.base_entity import BaseEntity


class Relation(Enum):
    EQUIVALENT = 0
    LESS = 1
    LESS_EQUAL = 2
    GREATER = 3
    GREATER_EQUAL = 4
    CONTAINS = 5


class SearchParameter(BaseEntity):
    def __init__(self, column: str = "", value="", relation: Relation = Relation.EQUIVALENT):
        super().__init__()
        self.column = column
        self.value = value
        self.relation: int | Relation = relation
        self.search_parameter_id: int | None = None
        self.search_parameter_collection_id: int | None = None

    def to_sql(self):
        """
        Turns the `SearchParameter` into a SQL WHERE-query constraint like "column = 'value'".
        """
        value = f"%{self.value}%" if self.relation == Relation.CONTAINS else self.value
        return f"`{self.column}` {self.equivalence_operator} '{value}'"

    @classmethod
    def from_row(cls, row: Row):
        """
        A constructor to make a SearchParameter from a sqlite Row `row`.
        """
        param = SearchParameter(row["column"], row["value"], Relation(int(row["relation"])))
        param.search_parameter_id = row["search_parameter_id"]
        param.search_parameter_collection_id = row["search_parameter_collection_id"]
        return param

    @property
    def equivalence_operator(self):
        match self.relation:
            case Relation.EQUIVALENT:
                return "="
            case Relation.LESS:
                return "<"
            case Relation.LESS_EQUAL:
                return "<="
            case Relation.GREATER:
                return ">"
            case Relation.GREATER_EQUAL:
                return ">="
            case Relation.CONTAINS:
                return "LIKE"
