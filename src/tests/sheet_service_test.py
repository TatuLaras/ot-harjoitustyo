import unittest
from unittest.mock import Mock

from entities.sheet import Sheet
from repositories.sheet_repository import SheetRepository
from services.sheet_service import SheetService
from sql_query_generators import (
    DuplicateHandling,
    sql_trivial_delete_generate,
    sql_trivial_id_select_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
    sql_trivial_select_with_params_generate,
)
from sql_search_params import SearchParameter


class TestSheetService(unittest.TestCase):
    """
    Tests the `SheetService` class with mocks.
    """

    def setUp(self):
        self.test_sheet = Sheet()
        self.test_sheet.title = "Title of sheet"

        another_sheet = Sheet()
        another_sheet.title = "searchparam"

        self.conn = Mock()
        result = Mock()
        result.fetchone = Mock(return_value=self.test_sheet.to_dict(False))
        result.fetchall = Mock(
            return_value=[self.test_sheet.to_dict(False), another_sheet.to_dict(False)]
        )
        self.conn.execute = Mock(return_value=result)
        repo = SheetRepository(self.conn)
        self.service: SheetService = SheetService(sheet_repository=repo)

    def test_get(self):
        self.assertEqual(self.service.get_sheet_by_id(6).title, self.test_sheet.title)

        self.conn.execute.assert_called_with(
            sql_trivial_id_select_generate("sheet", Sheet.columns(), "sheet_id", 6)
        )

    def test_get_all(self):
        self.assertEqual(self.service.get_all_sheets()[0].title, self.test_sheet.title)
        self.conn.execute.assert_called_with(sql_trivial_select_generate("sheet", Sheet.columns()))

    def test_create(self):
        self.service.create_sheet(self.test_sheet)

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate("sheet", [{"title": self.test_sheet.title}])
        )

    def test_update(self):
        self.service.update_sheet(self.test_sheet)

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate(
                "sheet",
                [{"title": self.test_sheet.title}],
                duplicate_handling=DuplicateHandling.UPDATE,
            )
        )

    def test_create_many(self):
        self.service.create_many_sheets([self.test_sheet, self.test_sheet])

        self.conn.execute.assert_called_with(
            sql_trivial_insert_generate(
                "sheet", [{"title": self.test_sheet.title}, {"title": self.test_sheet.title}]
            )
        )

    def test_delete(self):
        self.service.delete_sheet(6)

        self.conn.execute.assert_called_with(sql_trivial_delete_generate("sheet", "sheet_id", 6))

    def test_get_all_with_params(self):
        params = [
            SearchParameter("title", "searchparam"),
            SearchParameter("title", ""),
            SearchParameter("sheet_id", "asdf"),
        ]
        params_clean = [SearchParameter("title", "searchparam"), SearchParameter("sheet_id", 0)]
        self.service.get_all_sheets_with_params(params)
        self.conn.execute.assert_called_with(
            sql_trivial_select_with_params_generate("sheet", Sheet.columns(), params_clean)
        )

    def test_none_result(self):
        result = Mock()
        result.fetchone = Mock(return_value=None)
        self.conn.execute = Mock(return_value=result)
        self.assertIsNone(self.service.get_sheet_by_id(0))
