import dataclasses
import datetime


@dataclasses.dataclass
class Dates:
    despatch: datetime.datetime = None
    delivery: datetime.datetime = None

