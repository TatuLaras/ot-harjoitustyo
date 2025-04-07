import unittest

from entities.base_entity import BaseEntity


class ChildEntity(BaseEntity):
    def __init__(self) -> None:
        super().__init__()
        self.field_a = "value a"
        self.field_b = "value b"
        self.field_c = "value c"
        self.field_d = "value d"
        self.field_e = "value e"
        self.field_f = "value f"
        self.field_g = "value g"


class ChildEntityIgnored(BaseEntity):
    def __init__(self) -> None:
        super().__init__()
        self.field_a = "value a"
        self.field_b = "value b"
        self.field_c = "value c"
        self.field_d = "value d"
        self.field_e = "value e"
        self.field_f = "value f"
        self.field_g = "value g"
        self.ignored_field_a = "ignored a"
        self.ignored_field_b = "ignored b"
        self._BaseEntity__to_dict_ignore_fields = [
            "ignored_field_a",
            "ignored_field_b",
        ]


class ChildEntityNull(BaseEntity):
    def __init__(self) -> None:
        super().__init__()
        self.field_a = "value a"
        self.field_b = "value b"
        self.field_c = "value c"
        self.field_d = "value d"
        self.field_e = "value e"
        self.field_f = "value f"
        self.field_g = "value g"
        self.null_field = None


class TestBaseEntity(unittest.TestCase):
    """
    Tests to test functions of the inherited `BaseEntity`, mainly `to_dict`.
    """

    def setUp(self):
        self.correct = {
            "field_a": "value a",
            "field_b": "value b",
            "field_c": "value c",
            "field_d": "value d",
            "field_e": "value e",
            "field_f": "value f",
            "field_g": "value g",
        }

    def test_dict_is_correct(self):
        self.assertEqual(self.correct, ChildEntity().to_dict())

    def test_ignored_fields_ignored(self):
        self.assertEqual(self.correct, ChildEntityIgnored().to_dict())

    def test_null_fields_ignored(self):
        self.assertEqual(self.correct, ChildEntityNull().to_dict())

    def test_column_list(self):
        expected = [
            "field_a",
            "field_c",
            "field_d",
            "field_b",
            "field_e",
            "null_field",
            "field_f",
            "field_g",
        ]
        self.assertEqual(set(expected), set(ChildEntityNull.columns()))
