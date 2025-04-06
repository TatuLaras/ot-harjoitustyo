CREATE TABLE IF NOT EXISTS sheet_directory (
    sheet_directory_id INTEGER PRIMARY KEY,
    path TEXT
);

CREATE TABLE IF NOT EXISTS instrument (
    instrument_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS sheet (
    sheet_id INTEGER PRIMARY KEY,
    instrument_id INTEGER DEFAULT 0,
    file_path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    composer TEXT,
    genre TEXT,
    difficulty INTEGER,
    FOREIGN KEY (instrument_id) REFERENCES instrument(instrument_id)
);
