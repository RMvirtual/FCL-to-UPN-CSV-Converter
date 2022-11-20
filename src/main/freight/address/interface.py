from abc import ABC, abstractmethod


class Address(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self, new_name: str) -> None:
        ...

    @property
    @abstractmethod
    def lines(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def town(self) -> str:
        ...

    @town.setter
    @abstractmethod
    def town(self, new_town: str) -> None:
        ...

    @property
    @abstractmethod
    def post_code(self) -> str:
        ...

    @post_code.setter
    @abstractmethod
    def post_code(self, new_post_code: str) -> None:
        ...

    @property
    @abstractmethod
    def country(self) -> str:
        ...

    @country.setter
    @abstractmethod
    def country(self, new_country: str) -> None:
        ...

    @property
    @abstractmethod
    def contact_name(self) -> str:
        ...

    @contact_name.setter
    @abstractmethod
    def contact_name(self, new_contact_name: str) -> None:
        ...

    @property
    @abstractmethod
    def telephone_number(self) -> str:
        ...

    @telephone_number.setter
    @abstractmethod
    def telephone_number(self, new_telephone_number: str) -> None:
        ...
