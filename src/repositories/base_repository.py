from typing import Dict, List
from db import get_connection
from sql_query_generators import (
    sql_trivial_delete_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
)


class BaseRepository:
    def __init__(self) -> None:
        self.conn = get_connection()

    def trivial_select(self, table_name: str, columns: list[str]):
        query = sql_trivial_select_generate(table_name, columns)
        return self.conn.execute(query).fetchall()

    def trivial_insert(self, table_name: str, column_values: Dict):
        self.trivial_insert_many(table_name, [column_values])

    def trivial_insert_many(self, table_name: str, column_values: List[Dict]):
        query = sql_trivial_insert_generate(table_name, column_values)
        self.conn.execute(query)
        self.conn.commit()

    def trivial_delete(self, table_name: str, id_column: str, id_value: int):
        query = sql_trivial_delete_generate(table_name, id_column, id_value)
        self.conn.execute(query)
        self.conn.commit()
