import unittest
from unittest.mock import Mock

from entities.instrument import Instrument
from entities.sheet_directory import SheetDirectory
from repositories.settings_repository import SettingsRepository
from services.settings_service import SettingsService
from sql_query_generators import (
    sql_trivial_delete_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
)


class TestSettingsService(unittest.TestCase):
    """
    Tests the `SheetRepository` class with mocks.
    """

    def setUp(self):
        self.test_sheet_dir = SheetDirectory()
        self.test_sheet_dir.path = "/thisisapath"

        self.test_instrument = Instrument()
        self.test_instrument.name = "Guitar"

        self.conn = Mock()

        dir_result = Mock()
        dir_result.fetchone = Mock(return_value=self.test_sheet_dir.to_dict(False))
        dir_result.fetchall = Mock(return_value=[self.test_sheet_dir.to_dict(False)])

        instrument_result = Mock()
        instrument_result.fetchone = Mock(return_value=self.test_instrument.to_dict(False))
        instrument_result.fetchall = Mock(return_value=[self.test_instrument.to_dict(False)])

        self.conn.execute = Mock(
            side_effect=lambda query: (
                dir_result if "FROM `sheet_directory`" in query else instrument_result
            )
        )
        repo = SettingsRepository(self.conn)
        self.service = SettingsService(repo)

    def test_get_sheet_dirs(self):
        self.assertEqual(self.service.get_sheet_directories()[0].path, self.test_sheet_dir.path)

        self.conn.execute.assert_called_with(
            sql_trivial_select_generate("sheet_directory", SheetDirectory.columns())
        )

    def test_create_sheet_dir(self):
        self.service.create_sheet_directory("/newpath")

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate("sheet_directory", [{"path": "/newpath"}])
        )

    def test_delete_sheet_dir(self):
        self.service.delete_sheet_directory(self.test_sheet_dir.path)

        self.conn.execute.assert_called_with(
            sql_trivial_delete_generate("sheet_directory", "path", self.test_sheet_dir.path)
        )

    def test_get_instruments(self):
        self.assertEqual(self.service.get_instruments()[0].name, self.test_instrument.name)

        self.conn.execute.assert_called_with(
            sql_trivial_select_generate("instrument", Instrument.columns())
        )

    def test_create_instrument(self):
        self.service.create_instrument("newinstrument")
        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate("instrument", [{"name": "newinstrument"}])
        )

    def test_delete_instrument(self):
        self.service.delete_instrument(self.test_instrument.name)
        self.conn.execute.assert_called_with(
            sql_trivial_delete_generate("instrument", "name", self.test_instrument.name)
        )
