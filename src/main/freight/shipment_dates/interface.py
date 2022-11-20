import datetime
from abc import ABC, abstractmethod
from src.main.freight.shipment_dates.date.interface import Date


class ShipmentDates(ABC):
    @property
    @abstractmethod
    def delivery_date(self) -> Date:
        ...

    @delivery_date.setter
    @abstractmethod
    def delivery_date(self, new_date: str) -> None:
        ...

    @property
    @abstractmethod
    def collection_date(self) -> Date:
        ...

    @collection_date.setter
    @abstractmethod
    def collection_date(self, new_date: str) -> None:
        ...

    @property
    @abstractmethod
    def delivery_time(self) -> datetime.time:
        ...

    @delivery_time.setter
    @abstractmethod
    def delivery_time(self, new_time: str) -> None:
        ...
