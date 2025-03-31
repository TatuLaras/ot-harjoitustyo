from db import get_connection


class BaseRepository:
    def __init__(self) -> None:
        self.conn = get_connection()

    def trivial_select(self, table_name: str, columns: list[str]):
        query = f"SELECT {",".join(columns)} FROM {table_name}"
        return self.conn.execute(query).fetchall()
