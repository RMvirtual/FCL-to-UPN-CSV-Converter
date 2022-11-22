from abc import ABC, abstractmethod
from src.main.graylaw.address.interface import Address
from src.main.graylaw.references.interface import References
from src.main.graylaw.shipment_dates.interface import ShipmentDates
from src.main.graylaw.cargo.model import Cargo
from src.main.graylaw.service.model import Service


class Consignment(ABC):
    @property
    @abstractmethod
    def references(self) -> References:
        ...

    @property
    @abstractmethod
    def address(self) -> Address:
        ...

    @property
    @abstractmethod
    def cargo(self) -> Cargo:
        ...

    @property
    @abstractmethod
    def service(self) -> Service:
        ...

    @property
    @abstractmethod
    def delivery_instructions(self) -> list[str]:
        ...

    @property
    @abstractmethod
    def client_name(self) -> str:
        ...

    @property
    @abstractmethod
    def shipment_dates(self) -> ShipmentDates:
        ...
