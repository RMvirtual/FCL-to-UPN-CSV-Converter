from abc import abstractmethod
from src.main.companies.upn.interfaces.address import DeliveryAddressProvider
from src.main.companies.upn.interfaces.dates import DatesProvider
from src.main.companies.upn.interfaces.pallets import NetworkPallet, CustPallet
from src.main.companies.upn.interfaces.references import ReferencesUpload
from src.main.companies.upn.interfaces.services.container import \
    ServicesProvider


class BaseConsignment(
        DeliveryAddressProvider, ReferencesUpload, ServicesProvider,
        DatesProvider
):
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


class ConsignmentDownload(BaseConsignment):
    """Main interface for a consignment downloaded from the UPN
    system.
    """
    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_name(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> int:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[NetworkPallet]:
        ...


class ConsignmentUpload(BaseConsignment):
    """Main interface for a consignment to be uploaded to the UPN
    system.
    """
    @property
    @abstractmethod
    def paperwork_mode(self) -> int:
        ...

    @property
    @abstractmethod
    def short_description(self) -> str:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[CustPallet]:
        ...

    @property
    @abstractmethod
    def delivery_email(self) -> str:
        ...

