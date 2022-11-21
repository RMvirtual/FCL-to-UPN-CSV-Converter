from abc import ABC, abstractmethod
from src.main.graylaw.address.interface import Address
from src.main.graylaw.references.interface import References
from src.main.graylaw.cargo.model import Cargo
from src.main.graylaw.service.model import Service
from src.main.graylaw.shipment_dates.model import ShipmentDates


class Consignment(ABC):
    @property
    @abstractmethod
    def references(self) -> References:
        ...

    @references.setter
    @abstractmethod
    def references(self, new_references: References) -> None:
        ...

    @property
    @abstractmethod
    def address(self) -> Address:
        ...

    @address.setter
    @abstractmethod
    def address(self, new_address: Address) -> None:
        ...

    @property
    @abstractmethod
    def cargo(self) -> Cargo:
        ...

    @cargo.setter
    @abstractmethod
    def cargo(self, new_cargo: Cargo) -> None:
        ...

    @property
    @abstractmethod
    def service(self) -> Service:
        ...

    @service.setter
    @abstractmethod
    def service(self, new_service: Service) -> None:
        ...

    @property
    @abstractmethod
    def delivery_instructions(self) -> list[str]:
        ...

    @delivery_instructions.setter
    @abstractmethod
    def delivery_instructions(self, new_instructions: list[str]):
        ...

    @property
    @abstractmethod
    def client_name(self) -> str:
        ...

    @client_name.setter
    @abstractmethod
    def client_name(self, new_name: str) -> None:
        ...

    @property
    @abstractmethod
    def shipment_dates(self):
        ...

    @shipment_dates.setter
    @abstractmethod
    def shipment_dates(self, new_dates: ShipmentDates):
        ...
