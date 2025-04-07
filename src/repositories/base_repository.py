from typing import Dict, List
from db import get_connection
from sql_query_generators import (
    DuplicateHandling,
    sql_trivial_delete_generate,
    sql_trivial_id_select_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
)


class BaseRepository:
    def __init__(self, conn=get_connection()) -> None:
        self.conn = conn

    def trivial_id_select(self, table_name: str, columns: list[str], id_column: str, id_value: int):
        query = sql_trivial_id_select_generate(table_name, columns, id_column, id_value)
        return self.conn.execute(query).fetchone()

    def trivial_select(self, table_name: str, columns: list[str]):
        query = sql_trivial_select_generate(table_name, columns)
        return self.conn.execute(query).fetchall()

    def trivial_insert(
        self,
        table_name: str,
        column_values: Dict,
        duplicate_handling: DuplicateHandling = DuplicateHandling.IGNORE,
    ):
        self.trivial_insert_many(table_name, [column_values], duplicate_handling)

    def trivial_insert_many(
        self,
        table_name: str,
        column_values: List[Dict],
        duplicate_handling: DuplicateHandling = DuplicateHandling.IGNORE,
    ):
        query = sql_trivial_insert_generate(table_name, column_values, duplicate_handling)
        self.conn.execute(query)
        self.conn.commit()

    def trivial_delete(self, table_name: str, id_column: str, id_value: int):
        query = sql_trivial_delete_generate(table_name, id_column, id_value)
        self.conn.execute(query)
        self.conn.commit()
