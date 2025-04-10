from enum import Enum
from typing import Dict, List

from sql_search_params import SearchParameter, generate_where_query


class DuplicateHandling(Enum):
    IGNORE = 0
    UPDATE = 1


def sql_sanitize(string: str, allow_empty: bool = False) -> str:
    if len(string) == 0 and not allow_empty:
        raise ValueError("Trying to use an empty string to generate a SQL query")

    return string.replace("'", "").replace("`", "")


def sql_trivial_insert_generate(
    table_name: str,
    column_values: List[Dict],
    duplicate_handling: DuplicateHandling = DuplicateHandling.IGNORE,
) -> str:
    """
    Generates a basic insert query into `table_name` with data in
    `column_values`. `column_values` is expected to be a list of
    dictionaries that share the same keys, corresponding to the column
    names of table `table_name`.
    """

    if len(column_values) == 0:
        raise ValueError("column_values cannot be an empty list")

    table_name = sql_sanitize(table_name)
    column_list = ", ".join([f"`{sql_sanitize(x)}`" for x in column_values[0].keys()])
    values_list = ", ".join(
        [
            "(" + ", ".join([f"'{sql_sanitize(val, True)}'" for val in item.values()]) + ")"
            for item in column_values
        ]
    )

    policy = "IGNORE" if duplicate_handling == DuplicateHandling.IGNORE else "REPLACE"

    return f"INSERT OR {policy} INTO `{table_name}` ({column_list}) " + f"VALUES {values_list}"


def sql_trivial_delete_generate(table_name: str, id_column: str, id_value: int) -> str:
    """
    Generates a basic DELETE query to delete an entry from table
    `table_name` where column `id_column` is equal to `id_value`.
    """
    table_name = sql_sanitize(table_name)
    id_column = sql_sanitize(id_column)
    id_str = sql_sanitize(str(id_value))

    return f"DELETE FROM `{table_name}` WHERE `{id_column}` = '{id_str}'"


def sql_trivial_id_select_generate(
    table_name: str, columns: list[str], id_column: str, id_value: int
) -> str:
    """
    Generates a basic SELECT query that selects columns `columns` from table
    where column `id_column` is equal to `id_value`.
    """
    if len(columns) == 0:
        raise ValueError("List `columns` cannot be empty")

    table_name = sql_sanitize(table_name)
    id_column = sql_sanitize(id_column)
    id_str = sql_sanitize(str(id_value))
    column_list = ", ".join([f"`{sql_sanitize(col)}`" for col in columns])

    return f"SELECT {column_list} FROM `{table_name}` WHERE `{id_column}` = '{id_str}'"


def sql_trivial_select_generate(table_name: str, columns: list[str]) -> str:
    """
    Generates a basic SELECT query that selects columns `columns` from table
    `table_name`.
    """
    if len(columns) == 0:
        raise ValueError("List `columns` cannot be empty")

    table_name = sql_sanitize(table_name)
    column_list = ", ".join([f"`{sql_sanitize(col)}`" for col in columns])
    return f"SELECT {column_list} FROM `{table_name}`"


def sql_trivial_select_with_params_generate(
    table_name: str, columns: list[str], search_parameters: List[SearchParameter]
) -> str:
    where = generate_where_query(search_parameters)
    main_query = sql_trivial_select_generate(table_name, columns)
    return f"{main_query} WHERE {where}"
