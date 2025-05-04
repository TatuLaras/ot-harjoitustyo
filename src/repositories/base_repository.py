from typing import Dict, List
from db import get_connection
from sql_query_generators import (
    DuplicateHandling,
    sql_trivial_delete_generate,
    sql_trivial_id_select_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
    sql_trivial_select_with_params_generate,
)
from sql_search_params import SearchParameter


class BaseRepository:
    """
    A base class for all repositories, containing some common utility functions.
    """

    def __init__(self, conn=get_connection()) -> None:
        self.conn = conn

    def trivial_id_select(
        self, table_name: str, columns: list[str], id_column: str, id_value: int | str
    ):
        """
        Returns a sqlite Row of `columns` from table `table_name` in which the column `id_column` is
        equal to `id_value`.
        """
        query = sql_trivial_id_select_generate(table_name, columns, id_column, id_value)
        return self.conn.execute(query).fetchone()

    def trivial_select(self, table_name: str, columns: list[str]):
        """
        Returns a sqlite Row of `columns` from table `table_name`.
        """
        query = sql_trivial_select_generate(table_name, columns)
        return self.conn.execute(query).fetchall()

    def trivial_select_with_params(
        self, table_name: str, columns: list[str], search_parameters: List[SearchParameter]
    ):
        """
        Returns a sqlite Row of `columns` from table `table_name`, with WHERE conditions defined
        by `search_parameters`.
        """
        query = sql_trivial_select_with_params_generate(table_name, columns, search_parameters)
        return self.conn.execute(query).fetchall()

    def trivial_insert(
        self,
        table_name: str,
        column_values: Dict,
        duplicate_handling: DuplicateHandling = DuplicateHandling.IGNORE,
    ):
        """
        Same as trivial_insert_many, but with a single row / `column_values` to insert.
        """
        self.trivial_insert_many(table_name, [column_values], duplicate_handling)

    def trivial_insert_many(
        self,
        table_name: str,
        column_values: List[Dict],
        duplicate_handling: DuplicateHandling = DuplicateHandling.IGNORE,
    ):
        """
        Generates a basic insert query into `table_name` with data in
        `column_values`. `column_values` is expected to be a list of
        dictionaries that share the same keys, corresponding to the column
        names of table `table_name`.
        """
        if len(column_values) == 0:
            return

        query = sql_trivial_insert_generate(table_name, column_values, duplicate_handling)
        self.conn.execute(query)
        self.conn.commit()

    def trivial_delete(self, table_name: str, id_column: str, id_value: int | str):
        """
        Deletes an entry from table `table_name` where column `id_column` is equal to `id_value`.
        """
        query = sql_trivial_delete_generate(table_name, id_column, id_value)
        self.conn.execute(query)
        self.conn.commit()
