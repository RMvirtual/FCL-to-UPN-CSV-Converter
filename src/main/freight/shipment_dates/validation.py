from src.main.freight.shipment_dates.interface import ShipmentDatesInterface
from src.main.time.dates.factory import dates as factory


class ValidationStrategy:
    def __init__(self, dates: ShipmentDatesInterface):
        self._dates = dates

    def can_set_delivery_date(self, new_date: str) -> bool:
        new_delivery_date = factory.from_string(new_date)

        return (
            True if self.collection_date_empty()
            else new_delivery_date > self._dates.collection_date
        )

    def can_set_collection_date(self, new_date: str) -> bool:
        new_collection_date = factory.from_string(new_date)

        return (
            True if self.delivery_date_empty()
            else new_collection_date < self._dates.delivery_date
        )

    def collection_date_empty(self) -> bool:
        return not self._dates.collection_date

    def delivery_date_empty(self) -> bool:
        return not self._dates.delivery_date

    def assert_can_set_delivery_date(self, new_date: str) -> None:
        if not self.can_set_delivery_date(new_date):
            raise ValueError("Invalid date for delivery date.")

    def assert_can_set_collection_date(self, new_date: str) -> None:
        if not self.can_set_collection_date(new_date):
            raise ValueError("Invalid date for collection date.")
