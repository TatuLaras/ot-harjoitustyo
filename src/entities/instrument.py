from sqlite3 import Row
from entities.base_entity import BaseEntity


class Instrument(BaseEntity):
    def __init__(self):
        super().__init__()
        self.instrument_id: int | None = None
        self.name: str | None = None

    @classmethod
    def from_row(cls, row: Row):
        instrument = Instrument()
        instrument.instrument_id = row["instrument_id"]
        instrument.name = row["name"]
        return instrument
