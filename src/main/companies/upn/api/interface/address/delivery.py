from abc import ABC, abstractmethod


class DeliveryAddressProvider(ABC):
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
