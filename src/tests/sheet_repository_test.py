import unittest
from unittest.mock import Mock

from entities.sheet import Sheet
from repositories.sheet_repository import SheetRepository
from sql_query_generators import (
    DuplicateHandling,
    sql_trivial_delete_generate,
    sql_trivial_id_select_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
)


class TestSheetRepository(unittest.TestCase):
    """
    Tests the `SheetRepository` class with mocks.
    """

    def setUp(self):
        self.test_sheet = Sheet()
        self.test_sheet.title = "Title of sheet"

        self.conn = Mock()
        result = Mock()
        result.fetchone = Mock(return_value=self.test_sheet.to_dict(False))
        result.fetchall = Mock(return_value=[self.test_sheet.to_dict(False)])
        self.conn.execute = Mock(return_value=result)
        self.repo = SheetRepository(self.conn)

    def test_get(self):
        self.assertEqual(self.repo.get(6).title, self.test_sheet.title)

        self.conn.execute.assert_called_with(
            sql_trivial_id_select_generate("sheet", Sheet.columns(), "sheet_id", 6)
        )

    def test_get_all(self):
        self.repo = SheetRepository(self.conn)
        self.assertEqual(self.repo.get_all()[0].title, self.test_sheet.title)

        self.conn.execute.assert_called_with(sql_trivial_select_generate("sheet", Sheet.columns()))

    def test_create(self):
        self.repo = SheetRepository(self.conn)
        self.repo.create(self.test_sheet)

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate("sheet", [{"title": self.test_sheet.title}])
        )

    def test_update(self):
        self.repo = SheetRepository(self.conn)
        self.repo.update(self.test_sheet)

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate(
                "sheet",
                [{"title": self.test_sheet.title}],
                duplicate_handling=DuplicateHandling.UPDATE,
            )
        )

    def test_create_many(self):
        self.repo = SheetRepository(self.conn)
        self.repo.create_many([self.test_sheet, self.test_sheet])

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate(
                "sheet", [{"title": self.test_sheet.title}, {"title": self.test_sheet.title}]
            )
        )

    def test_delete(self):
        self.repo = SheetRepository(self.conn)
        self.repo.delete(6)

        self.conn.execute.assert_called_with(sql_trivial_delete_generate("sheet", "sheet_id", 6))
