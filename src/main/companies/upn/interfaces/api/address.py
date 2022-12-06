from abc import ABC, abstractmethod


class UPNAddressable(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def line_1(self) -> str:
        ...

    @property
    @abstractmethod
    def line_2(self) -> str:
        ...

    @property
    @abstractmethod
    def town(self) -> str:
        ...

    @property
    @abstractmethod
    def county(self) -> str:
        ...

    @property
    @abstractmethod
    def post_code(self) -> str:
        ...

    @property
    @abstractmethod
    def country(self) -> str:
        ...

    @property
    @abstractmethod
    def contact_name(self) -> str:
        ...

    @property
    @abstractmethod
    def telephone_no(self) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self, new_name: str) -> None:
        ...

    @line_1.setter
    @abstractmethod
    def line_1(self, new_line: str) -> None:
        ...

    @line_2.setter
    @abstractmethod
    def line_2(self, new_line: str) -> None:
        ...

    @town.setter
    @abstractmethod
    def town(self, new_town: str) -> None:
        ...

    @county.setter
    @abstractmethod
    def county(self, new_county: str) -> None:
        ...

    @post_code.setter
    @abstractmethod
    def post_code(self, new_post_code: str) -> None:
        ...

    @country.setter
    @abstractmethod
    def country(self, new_country: str) -> None:
        ...

    @contact_name.setter
    @abstractmethod
    def contact_name(self, new_contact_name: str) -> None:
        ...

    @telephone_no.setter
    @abstractmethod
    def telephone_no(self, new_number: str) -> None:
        ...


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

