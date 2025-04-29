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

CREATE TABLE IF NOT EXISTS search_parameter_collection (
    search_parameter_collection_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS search_parameter (
    search_parameter_id INTEGER PRIMARY KEY,
    search_parameter_collection_id INTEGER,
    column TEXT NOT NULL,
    value TEXT NOT NULL,
    relation INTEGER NOT NULL,
    FOREIGN KEY(search_parameter_collection_id)
        REFERENCES search_parameter_collection(search_parameter_collection_id)
);
