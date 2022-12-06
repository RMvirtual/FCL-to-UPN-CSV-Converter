from abc import ABC, abstractmethod


class NetworkConsignmentKeyMap(ABC):
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
    def depot_no(self) -> str:
        ...

    @property
    @abstractmethod
    def despatch_date(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_datetime(self) -> str:
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
    def delivery_country(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_contact_name(self) -> str:
        ...

    @property
    @abstractmethod
    def delivery_telephone_no(self) -> str:
        ...

    @property
    @abstractmethod
    def total_weight(self) -> str:
        ...

    @property
    @abstractmethod
    def special_instructions(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_id(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_name(self) -> str:
        ...

    @property
    @abstractmethod
    def customer_paperwork_pages(self) -> str:
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
    def pallets(self) -> str:
        ...
