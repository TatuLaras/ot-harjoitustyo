from sqlite3 import Row
from entities.base_entity import BaseEntity


class Instrument(BaseEntity):
    """
    Models a single user-defined instrument in settings,
    corresponding to the database table instrument.
    """

    def __init__(self):
        super().__init__()
        self.instrument_id: int | None = None
        self.name: str | None = None

    @classmethod
    def from_row(cls, row: Row):
        """
        A constructor to make an Instrument from a sqlite `row`.
        """
        instrument = Instrument()
        instrument.instrument_id = row["instrument_id"]
        instrument.name = row["name"]
        return instrument
