from __future__ import annotations
import datetime

from src.main.freight.shipment_dates.date.interface.interface \
    import Date as DateInterface

from src.main.freight.shipment_dates.date.implementation.implementation import Date


class ShipmentDates:
    def __init__(self):
        self._collection_date: DateInterface or None = None
        self._delivery_date: DateInterface or None = None
        self._delivery_time: datetime.time or None = None

    @property
    def delivery_date(self) -> DateInterface:
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, new_date: str) -> None:
        self._delivery_date = Date(new_date)

    @property
    def collection_date(self) -> DateInterface:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: str) -> None:
        if self._delivery_date is not None and self._delivery_date < new_date:
            raise ValueError(
                "Collection date cannot be later than delivery date.")

        self._collection_date = Date(new_date)

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: str) -> None:
        self._delivery_time = datetime.datetime.strptime(new_time, "%I:%M%p")
