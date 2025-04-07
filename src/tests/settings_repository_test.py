import unittest
from unittest.mock import Mock

from entities.sheet import Sheet
from entities.sheet_directory import SheetDirectory
from repositories.settings_repository import SettingsRepository
from repositories.sheet_repository import SheetRepository
from sql_query_generators import (
    sql_trivial_delete_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
)


class TestSheetRepository(unittest.TestCase):
    """
    Tests the `SheetRepository` class with mocks.
    """

    def setUp(self):
        self.test_sheet_dir = SheetDirectory()
        self.test_sheet_dir.path = "/thisisapath"

        self.conn = Mock()
        result = Mock()
        result.fetchone = Mock(return_value=self.test_sheet_dir.to_dict(False))
        result.fetchall = Mock(return_value=[self.test_sheet_dir.to_dict(False)])
        self.conn.execute = Mock(return_value=result)
        self.repo = SettingsRepository(self.conn)

    def test_get_sheet_dirs(self):
        self.assertEqual(self.repo.get_sheet_directories()[0].path, self.test_sheet_dir.path)

        self.conn.execute.assert_called_with(
            sql_trivial_select_generate("sheet_directory", SheetDirectory.columns())
        )

    def test_create_sheet_dir(self):
        self.assertEqual(self.repo.get_sheet_directories()[0].path, self.test_sheet_dir.path)
        self.repo.create_sheet_directory("/newpath")

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate("sheet_directory", [{"path": "/newpath"}])
        )

    def test_delete_sheet_dir(self):
        self.assertEqual(self.repo.get_sheet_directories()[0].path, self.test_sheet_dir.path)
        self.repo.delete_sheet_directory(7)

        self.conn.execute.assert_called_with(
            sql_trivial_delete_generate("sheet_directory", "sheet_directory_id", 7)
        )
