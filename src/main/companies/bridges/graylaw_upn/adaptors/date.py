import copy
import datetime
from src.main.freight.shipment_dates.date.interfaces.interface import Date as GraylawDate
from src.main.freight.shipment_dates.date.model.comparison \
    import ComparisonStrategy


class UPNDateAdaptor(GraylawDate):
    def __init__(self, upn_date: datetime.datetime):
        self._date = copy.deepcopy(upn_date)
        self._comparison= ComparisonStrategy(self)

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
        return self._comparison.difference_in_days(other)

    def __eq__(self, other: GraylawDate) -> bool:
        return self._comparison.is_equal_to(other)

    def __lt__(self, other: GraylawDate) -> bool:
        return self._comparison.is_less_than(other)

    def __le__(self, other: GraylawDate) -> bool:
        return self._comparison.is_less_than_equal_to(other)

    def __ge__(self, other: GraylawDate) -> bool:
        return self._comparison.is_greater_than_equal_to(other)

    def __gt__(self, other: GraylawDate) -> bool:
        return self._comparison.is_greater_than(other)
