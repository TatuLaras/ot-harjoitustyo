class BaseEntity:
    def __init__(self) -> None:
        self.__to_dict_ignore_fields = []

    def to_dict(self):
        """
        Returns a dictionary of the entitys fields, excluding fields listed in `BaseEntity.to_dict_ignore_fields`
        """
        fields = self.__dict__
        return_dict = dict()

        # Filter out non database bound fields
        for key, value in fields.items():
            if key in self.__to_dict_ignore_fields:
                continue
            if key.startswith("_BaseEntity"):
                continue
            if value is None:
                continue

            return_dict[key] = value

        return return_dict
