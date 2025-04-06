import os

from entities.sheet import Sheet


def scan_directory_for_sheets(path: str):
    """
    Scans directory at `path` recursively for pdf files, returning a list of
    Sheet objects corresponding to the files
    """
    sheets = []

    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if not filename.endswith(".pdf"):
                continue

            sheet_path = os.path.join(dirpath, filename)
            sheet = Sheet.from_filepath(sheet_path)
            sheet.title = filename.removesuffix(".pdf")
            sheets.append(sheet)

    return sheets
