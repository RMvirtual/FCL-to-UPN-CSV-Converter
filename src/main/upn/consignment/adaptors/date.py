import copy
import datetime
from src.main.graylaw.shipment_dates.date.interface import Date as GraylawDate


class UPNDateAdaptor(GraylawDate):
    def __init__(self, upn_date: datetime.datetime):
        self._date = copy.deepcopy(upn_date)

    @property
    def day(self) -> int:
        return self._date.day

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def year(self) -> int:
        return self._date.year

    def __sub__(self, other: GraylawDate) -> int:
        ...

    def __eq__(self, other: GraylawDate) -> bool:
        return False

    def __lt__(self, other: GraylawDate) -> bool:
        return False

    def __le__(self, other: GraylawDate) -> bool:
        return False

    def __ge__(self, other: GraylawDate) -> bool:
        return False

    def __gt__(self, other: GraylawDate) -> bool:
        return False
