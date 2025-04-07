import unittest

from utils import flatten


class TestUtilities(unittest.TestCase):
    """
    Test miscellaneous utilities
    """

    def test_flatten(self):
        nonevalue = None
        string = "string abc"
        self.assertEqual(flatten(nonevalue), "")
        self.assertEqual(flatten(string), string)
