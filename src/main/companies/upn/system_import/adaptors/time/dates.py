import datetime
from src.main.companies.upn.interfaces.dates import UPNDates
from src.main.freight.shipment_dates.interface import ShipmentDatesInterface
from src.main.time.dates.interface.date import DateInterface
from src.main.companies.upn.system_import.adaptors.time.date \
    import UPNDateAdaptor


class UPNDatesInterfaceAdaptor(ShipmentDatesInterface):
    """Adaptor for turning a UPN Dates structure into a Graylaw
    Shipment Dates structure.
    """
    def __init__(self, upn_dates: UPNDates):
        self._dates = upn_dates

    @property
    def delivery_date(self) -> DateInterface:
        return UPNDateAdaptor(self._dates.delivery.date())

    @property
    def collection_date(self) -> DateInterface:
        return UPNDateAdaptor(self._dates.despatch)

    @property
    def delivery_time(self) -> datetime.time:
        return self._dates.delivery.time()

