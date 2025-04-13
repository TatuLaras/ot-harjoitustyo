import unittest

from entities.sheet import Sheet


class TestSheet(unittest.TestCase):
    def test_from_filepath(self):
        filepath = "/filepath"
        expected = Sheet()
        expected.title = ""
        expected.file_path = filepath

        self.assertEqual(Sheet.from_filepath(filepath).to_dict(), expected.to_dict())
