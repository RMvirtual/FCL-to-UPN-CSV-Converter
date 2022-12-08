from abc import abstractmethod
from src.main.companies.upn.api.interface.address.delivery \
    import DeliveryAddressProvider
from src.main.companies.upn.api.interface.dates.dates import DatesProvider
from src.main.companies.upn.api.interface.service.options \
    import ServiceOptions


class BaseConsignment(
        DeliveryAddressProvider, ServiceOptions, DatesProvider):
    """Base Interface for UPN Consignment interfaces to draw common
    functionality from (ConNo, Del address etc).
    """
    @property
    @abstractmethod
    def depot_no(self) -> int:
        ...

    @property
    @abstractmethod
    def customer_id(self) -> int:
        ...

    @property
    @abstractmethod
    def special_instructions(self) -> str:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> int:
        ...
