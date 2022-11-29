import datetime
from src.main.companies.upn.freight.dates.dates import UPNDates
from src.main.freight.shipment_dates.container.interface import ShipmentDates
from src.main.freight.shipment_dates.date.interface import Date as GraylawDate
from src.main.companies.bridges.graylaw_upn.adaptors.date import UPNDateAdaptor


class UPNDatesAdaptor(ShipmentDates):
    """Adaptor for turning a UPN Dates structure into a Graylaw
    Shipment Dates structure.
    """
    def __init__(self, upn_dates: UPNDates):
        self._dates = upn_dates

    @property
    def delivery_date(self) -> GraylawDate:
        return UPNDateAdaptor(self._dates.delivery.date())

    @property
    def collection_date(self) -> GraylawDate:
        return UPNDateAdaptor(self._dates.despatch)

    @property
    def delivery_time(self) -> datetime.time:
        return self._dates.delivery.time()

