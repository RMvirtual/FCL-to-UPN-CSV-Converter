import dataclasses
import datetime


@dataclasses.dataclass
class UPNDates:
    despatch: datetime.datetime = None
    delivery: datetime.datetime = None

