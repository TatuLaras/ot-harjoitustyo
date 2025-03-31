from typing import Dict, List


def sql_sanitize(string: str) -> str:
    if len(string) == 0:
        raise ValueError(
            "Trying to use an empty string to generate a SQL query"
        )

    return string.replace("'", "").replace("`", "")


def sql_trivial_insert_generate(
    table_name: str, column_values: List[Dict]
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
    column_list = ", ".join(
        [f"`{sql_sanitize(x)}`" for x in column_values[0].keys()]
    )
    values_list = ", ".join(
        [
            "("
            + ", ".join([f"'{sql_sanitize(val)}'" for val in item.values()])
            + ")"
            for item in column_values
        ]
    )

    return (
        f"INSERT OR IGNORE INTO `{table_name}` ({column_list}) "
        + f"VALUES {values_list}"
    )


def sql_trivial_delete_generate(
    table_name: str, id_column: str, id_value: int
) -> str:
    """
    Generates a basic DELETE query to delete an entry from table
    `table_name` where column `id_column` is equal to `id_value`.
    """
    table_name = sql_sanitize(table_name)
    id_column = sql_sanitize(id_column)
    id = sql_sanitize(str(id_value))

    return f"DELETE FROM `{table_name}` WHERE `{id_column}` = '{id}'"


def sql_trivial_select_generate(table_name: str, columns: list[str]) -> str:
    """
    Generates a basic SELECT query that selects columns `columns` from table
    `table_name`.
    """
    table_name = sql_sanitize(table_name)
    column_list = ", ".join([f"`{sql_sanitize(col)}`" for col in columns])
    return f"SELECT {column_list} FROM `{table_name}`"
