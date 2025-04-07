import unittest

from sql_search_params import Constraint, SearchParameter, generate_where_query


class TestSearchParams(unittest.TestCase):
    """
    Tests the SQL query parameter generation
    """

    def setUp(self):
        pass

    def test_output_correct(self):
        params = [
            SearchParameter("id", 4, Constraint.LessEqual),
            SearchParameter("name", "Maija"),
            SearchParameter("company", "Company co."),
        ]
        expected = "`id` <= '4' AND `name` = 'Maija' AND `company` = 'Company co.'"
        self.assertEqual(expected, generate_where_query(params))
        pass

    def test_works_for_empty_list(self):
        self.assertEqual("1=1", generate_where_query([]))

    def test_constraints_correct(self):
        params = [
            SearchParameter("val_1", 1, Constraint.LessEqual),
            SearchParameter("val_2", 2, Constraint.Equivalent),
            SearchParameter("val_3", 3, Constraint.Less),
            SearchParameter("val_4", 4, Constraint.LessEqual),
            SearchParameter("val_5", 5, Constraint.Greater),
            SearchParameter("val_6", 6, Constraint.GreaterEqual),
        ]
        expected = "`val_1` <= '1' AND `val_2` = '2' AND `val_3` < '3' AND `val_4` <= '4' AND `val_5` > '5' AND `val_6` >= '6'"
        self.assertEqual(expected, generate_where_query(params))

    def test_str_values_have_constraint_flattened_to_equal(self):
        params = [
            SearchParameter("val_1", "1", Constraint.LessEqual),
            SearchParameter("val_2", "2", Constraint.Equivalent),
            SearchParameter("val_3", "3", Constraint.Less),
            SearchParameter("val_4", "4", Constraint.LessEqual),
            SearchParameter("val_5", "5", Constraint.Greater),
            SearchParameter("val_6", "6", Constraint.GreaterEqual),
        ]
        expected = "`val_1` = '1' AND `val_2` = '2' AND `val_3` = '3' AND `val_4` = '4' AND `val_5` = '5' AND `val_6` = '6'"
        self.assertEqual(expected, generate_where_query(params))
        pass
