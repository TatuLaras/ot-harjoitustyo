import sqlite3
import os
from pathlib import Path

SCHEMA_FILE = os.path.join(os.path.dirname(__file__), "schema.sql")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

# Create data directory if it doesn't exist
Path(DATA_DIR).mkdir(exist_ok=True, parents=True)

conn = sqlite3.connect(os.path.join(DATA_DIR, "db.sqlite"))
conn.row_factory = sqlite3.Row


def get_connection() -> sqlite3.Connection:
    """
    Connects to the sqlite database file in `database_file` and returns the
    connection.
    """
    return conn


def init_schema():
    """
    Runs the SQL script in `schema_file_path` on the `conn`, initializing the
    necessary tables in the SQLite database.
    """
    with open(SCHEMA_FILE, "r", encoding="utf-8") as fp:
        contents = fp.read()
        conn.executescript(contents)
