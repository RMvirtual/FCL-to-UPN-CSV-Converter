import copy
from src.main.upn.consignment.structures.dates import UPNDates
from src.main.graylaw.shipment_dates.interface import ShipmentDates


class UPNDatesAdaptor(ShipmentDates):
    """Adaptor for turning a UPN Dates structure into a Graylaw
    Shipment Dates structure.
    """
    def __init__(self, upn_dates: UPNDates):
        self._dates = upn_dates

    @property
    def delivery_date(self) -> Date:
        ...

    @delivery_date.setter
    def delivery_date(self, new_date: str) -> None:
        ...

    @property
    def collection_date(self) -> Date:
        ...

    @collection_date.setter
    def collection_date(self, new_date: str) -> None:
        ...

    @property
    def delivery_time(self) -> datetime.time:
        ...

    @delivery_time.setter
    def delivery_time(self, new_time: str) -> None:
        ...
