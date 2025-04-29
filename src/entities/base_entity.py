from typing import List


class BaseEntity:
    """
    A common base entity with some common utility methods.
    """

    def __init__(self) -> None:
        self.__to_dict_ignore_fields = []

    def to_dict(self, ignore_nones=True):
        """
        Returns a dictionary of the entitys fields, excluding fields listed in
        `BaseEntity.to_dict_ignore_fields`
        """
        fields = self.__dict__
        return_dict = {}

        # Filter out non database bound fields
        for key, value in fields.items():
            if key in self.__to_dict_ignore_fields:
                continue
            if key.startswith("_BaseEntity"):
                continue
            if value is None and ignore_nones:
                continue

            return_dict[key] = str(value)

        return return_dict

    @classmethod
    def columns(cls) -> List[str]:
        dummy = cls()
        return list(dummy.to_dict(False).keys())
