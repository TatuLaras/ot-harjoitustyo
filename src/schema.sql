CREATE TABLE IF NOT EXISTS sheet_directory (
    sheet_directory_id INTEGER PRIMARY KEY,
    path TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS instrument (
    instrument_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS sheet (
    sheet_id INTEGER PRIMARY KEY,
    instrument_id INTEGER DEFAULT 0,
    file_path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    composer TEXT,
    genre TEXT,
    difficulty INTEGER,
    instrument TEXT
);
