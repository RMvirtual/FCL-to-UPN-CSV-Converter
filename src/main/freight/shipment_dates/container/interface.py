import datetime
from abc import ABC, abstractmethod
from src.main.time.dates.interface.date import DateInterface


class ShipmentDates(ABC):
    @property
    @abstractmethod
    def delivery_date(self) -> DateInterface:
        ...

    @delivery_date.setter
    @abstractmethod
    def delivery_date(self, dd_mm_yyyy: str) -> None:
        ...

    @property
    @abstractmethod
    def collection_date(self) -> DateInterface:
        ...

    @collection_date.setter
    @abstractmethod
    def collection_date(self, dd_mm_yyyy: str) -> None:
        ...

    @property
    @abstractmethod
    def delivery_time(self) -> datetime.time:
        ...
