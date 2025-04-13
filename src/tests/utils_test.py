import unittest

from utils import flatten, safe_cast_to_int


class TestUtilities(unittest.TestCase):
    """
    Test miscellaneous utilities
    """

    def test_flatten(self):
        nonevalue = None
        string = "string abc"
        self.assertEqual(flatten(nonevalue), "")
        self.assertEqual(flatten(string), string)

    def test_safe_cast_to_int(self):
        self.assertEqual(123, safe_cast_to_int(123))
        self.assertEqual(123, safe_cast_to_int("123"))
        self.assertEqual(0, safe_cast_to_int("asdasd"))
        self.assertEqual(0, safe_cast_to_int(""))
