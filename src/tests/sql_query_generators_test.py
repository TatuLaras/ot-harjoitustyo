import unittest

from sql_query_generators import (
    sql_trivial_delete_generate,
    sql_trivial_id_select_generate,
    sql_trivial_insert_generate,
    sql_trivial_select_generate,
    sql_trivial_select_with_params_generate,
)
from sql_search_params import Constraint, SearchParameter


class TestQueryGenerators(unittest.TestCase):
    """
    Tests the SQL query generators
    """

    def setUp(self):
        pass

    def test_trivial_select_is_correct(self):
        query = sql_trivial_select_generate(
            "testing_table", ["test_col_a", "test_col_b", "test_col_c"]
        )
        self.assertEqual(
            query,
            "SELECT `test_col_a`, `test_col_b`, `test_col_c` FROM `testing_table`",
        )

    def test_trivial_select_with_params_is_correct(self):
        query = sql_trivial_select_with_params_generate(
            "testing_table",
            ["test_col_a", "test_col_b", "test_col_c"],
            [
                SearchParameter("test_col_a", 4, Constraint.GREATER_EQUAL),
                SearchParameter("test_col_b", "val", Constraint.CONTAINS),
            ],
        )
        self.assertEqual(
            query,
            "SELECT `test_col_a`, `test_col_b`, `test_col_c` FROM `testing_table` WHERE `test_col_a` >= '4' AND `test_col_b` LIKE '%val%'",
        )

    def test_trivial_id_select_is_correct(self):
        query = sql_trivial_id_select_generate(
            "testing_table", ["test_col_a", "test_col_b", "test_col_c"], "test_id", 5
        )
        self.assertEqual(
            query,
            "SELECT `test_col_a`, `test_col_b`, `test_col_c` FROM `testing_table` WHERE `test_id` = '5'",
        )

    def test_trivial_delete_is_correct(self):
        query = sql_trivial_delete_generate("testing_table", "testing_table_id_column", "1234")
        self.assertEqual(
            query,
            "DELETE FROM `testing_table` WHERE `testing_table_id_column` = '1234'",
        )

    def test_trivial_insert_is_correct_one_entry(self):
        query = sql_trivial_insert_generate(
            "testing_table",
            [
                {
                    "column_a": "value of column a",
                    "column_b": "value of column b",
                    "column_c": "value of column c",
                },
            ],
        )
        self.assertEqual(
            query,
            "INSERT OR IGNORE INTO `testing_table` "
            + "(`column_a`, `column_b`, `column_c`) VALUES "
            + "('value of column a', 'value of column b', 'value of column c')",
        )

    def test_trivial_insert_is_correct_many_entries(self):
        query = sql_trivial_insert_generate(
            "testing_table",
            [
                {
                    "column_a": "value of column a",
                    "column_b": "value of column b",
                    "column_c": "value of column c",
                },
                {
                    "column_a": "second value of column a",
                    "column_b": "second value of column b",
                    "column_c": "second value of column c",
                },
                {
                    "column_a": "third value of column a",
                    "column_b": "third value of column b",
                    "column_c": "third value of column c",
                },
            ],
        )
        self.assertEqual(
            query,
            "INSERT OR IGNORE INTO `testing_table` "
            + "(`column_a`, `column_b`, `column_c`) VALUES "
            + "('value of column a', 'value of column b', 'value of column c'), "
            + "('second value of column a', 'second value of column b', 'second value of column c'), "
            + "('third value of column a', 'third value of column b', 'third value of column c')",
        )

    def test_trivial_delete_string_escape(self):
        query = sql_trivial_delete_generate("testing_table`", "`testing_table_id_column", "12'34")
        self.assertEqual(
            query,
            "DELETE FROM `testing_table` WHERE `testing_table_id_column` = '1234'",
        )

    def test_trivial_select_string_escape(self):
        query = sql_trivial_select_generate(
            "tes`ting_table", ["test'''_col_a", "tes'`t_col_b", "test_col_c'"]
        )
        self.assertEqual(
            query,
            "SELECT `test_col_a`, `test_col_b`, `test_col_c` FROM `testing_table`",
        )

    def test_trivial_id_select_string_escape(self):
        query = sql_trivial_id_select_generate(
            "tes`ting_table", ["test'''_col_a", "tes'`t_col_b", "test_col_c'"], "ta'`ble_id", "1`'3"
        )
        self.assertEqual(
            query,
            "SELECT `test_col_a`, `test_col_b`, `test_col_c` FROM `testing_table` WHERE `table_id` = '13'",
        )

    def test_trivial_insert_string_escape(self):
        query = sql_trivial_insert_generate(
            "testing_table",
            [
                {
                    "col'`umn_a": "value o''`f column a",
                    "col'`umn_b": "value of 'column b",
                    "col'`umn_c": "'value of column c",
                },
            ],
        )
        self.assertEqual(
            query,
            "INSERT OR IGNORE INTO `testing_table` "
            + "(`column_a`, `column_b`, `column_c`) VALUES "
            + "('value of column a', 'value of column b', 'value of column c')",
        )

    def test_trivial_insert_throws_error_on_empty_data(self):
        with self.assertRaises(ValueError):
            sql_trivial_insert_generate("testing_table", [])

    def test_trivial_queries_throws_error_on_empty_strings(self):
        with self.assertRaises(ValueError):
            sql_trivial_insert_generate(
                "",
                [
                    {
                        "col'`umn_a": "value o''`f column a",
                    },
                ],
            )

        with self.assertRaises(ValueError):
            sql_trivial_delete_generate("table", "asd", "")

        with self.assertRaises(ValueError):
            sql_trivial_select_generate("table", ["hello", ""])

        with self.assertRaises(ValueError):
            sql_trivial_id_select_generate("table", ["hello", "asd"], "", 4)

    def test_trivial_selects_throw_on_empty_column_list(self):
        with self.assertRaises(ValueError):
            sql_trivial_id_select_generate("table", [], "table", 4)

        with self.assertRaises(ValueError):
            sql_trivial_select_generate("table", [])
