import datetime
from abc import ABC, abstractmethod
from src.main.freight.shipment_dates.date.interface import Date


class ShipmentDates(ABC):
    @property
    @abstractmethod
    def delivery_date(self) -> Date:
        ...

    @property
    @abstractmethod
    def collection_date(self) -> Date:
        ...

    @property
    @abstractmethod
    def delivery_time(self) -> datetime.time:
        ...
