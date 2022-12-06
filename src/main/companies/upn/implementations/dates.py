from datetime import datetime
from src.main.companies.upn.interfaces.api.dates import DatesProvider


class UPNDates(DatesProvider):
    def __init__(self, despatch: datetime, delivery: datetime) -> None:
        self._despatch = despatch
        self._delivery = delivery

    @property
    def despatch_date(self) -> datetime:
        return self._despatch

    @property
    def delivery_datetime(self) -> datetime:
        return self._delivery
