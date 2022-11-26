import datetime
from abc import ABC, abstractmethod
from src.main.upn.api.data_structures.interfaces.network_pallet \
    import NetworkPalletInterface


class NetworkConsignmentInterface(ABC):
    """Main interface for the UPN Network Consignment structure
    returned through the UPN API.
    """
    @property
    @abstractmethod
    def consignment_no(self) -> str:
        ...

    @property
    @abstractmethod
    def barcode(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_reference(self) -> str:
        ...

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
    def customer_name(self) -> str:
        ...

    @property
    @abstractmethod
    def despatch_date(self) -> datetime.datetime:
        ...

    @property
    @abstractmethod
    def delivery_datetime(self) -> datetime.datetime:
        ...

    @property
    @abstractmethod
    def delivery_name(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_address_1(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_address_2(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_town(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_county(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_post_code(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_telephone_no(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_contact_name(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_country(self) -> str:
        ...

    @property
    @abstractmethod
    def special_instructions(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> int:
        ...

    @property
    @abstractmethod
    def main_service(self) -> str:
        ...

    @property
    @abstractmethod
    def premium_service(self) -> str:
        ...

    @property
    @abstractmethod
    def tail_lift_required(self) -> str:
        ...

    @property
    @abstractmethod
    def additional_service(self) -> str:
        ...

    @property
    @abstractmethod
    def pallets(self) -> list[NetworkPalletInterface]:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> int:
        ...
