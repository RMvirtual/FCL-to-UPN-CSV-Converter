from __future__ import annotations
import datetime
from src.main.freight.shipment_dates.interface import ShipmentDatesInterface
from src.main.freight.shipment_dates.validation import ValidationStrategy
from src.main.time.dates.factory import dates as dates_factory
from src.main.time.dates.interface.date import DateInterface


class ShipmentDates(ShipmentDatesInterface):
    def __init__(self):
        self._collection_date = None
        self._delivery_date = None
        self._delivery_time: datetime.time or None = None
        self._validator = ValidationStrategy(self)

    @property
    def delivery_date(self) -> DateInterface:
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, new_date: str) -> None:
        self._validator.assert_can_set_delivery_date(new_date)
        self._delivery_date = dates_factory.from_string(new_date)

    @property
    def collection_date(self) -> DateInterface:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: str) -> None:
        self._validator.assert_can_set_collection_date(new_date)
        self._collection_date = dates_factory.from_string(new_date)

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: str) -> None:
        self._delivery_time = datetime.datetime.strptime(new_time, "%I:%M%p")
