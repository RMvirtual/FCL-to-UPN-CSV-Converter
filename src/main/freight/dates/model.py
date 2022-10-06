import datetime


class ShipmentDates:
    def __init__(self):
        self._collection_date: datetime.date or None = None
        self._delivery_date: datetime.date or None = None
        self._delivery_time: datetime.time or None = None

    @property
    def delivery_date(self) -> datetime.date:
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, new_date: datetime.date) -> None:
        self._delivery_date = new_date

    @property
    def collection_date(self) -> datetime.date:
        return self._collection_date

    @collection_date.setter
    def collection_date(self, new_date: datetime.date) -> None:
        self._collection_date = new_date

    @property
    def delivery_time(self) -> datetime.time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, new_time: datetime.time) -> None:
        self._delivery_time = new_time
