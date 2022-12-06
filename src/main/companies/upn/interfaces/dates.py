import datetime
from abc import ABC, abstractmethod


class DatesProvider(ABC):
    @property
    @abstractmethod
    def despatch_date(self) -> datetime.datetime:
        ...

    @property
    @abstractmethod
    def delivery_datetime(self) -> datetime.datetime:
        ...
