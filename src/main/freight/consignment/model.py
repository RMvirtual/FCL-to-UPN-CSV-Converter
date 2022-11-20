from src.main.freight.consignment import interface
from src.main.freight.address.model import Address
from src.main.freight.address.interface import Address as AddressInterface
from src.main.freight.references.model import References
from src.main.freight.cargo.model import Cargo
from src.main.freight.service.model import Service
from src.main.freight.shipment_dates.model import ShipmentDates


class Consignment(interface.Consignment):
    def __init__(self, consignment_reference: str):
        self._references = References(consignment_reference)
        self._client_name = ""
        self._address = Address()
        self._cargo = Cargo()
        self._service = Service()
        self._shipment_dates = ShipmentDates()
        self._delivery_instructions: list[str] = []

    @property
    def references(self) -> References:
        return self._references

    @references.setter
    def references(self, new_references: References) -> None:
        self._references = new_references

    @property
    def address(self) -> AddressInterface:
        return self._address

    @address.setter
    def address(self, new_address: AddressInterface) -> None:
        self._address = new_address

    @property
    def cargo(self) -> Cargo:
        return self._cargo

    @cargo.setter
    def cargo(self, new_cargo: Cargo) -> None:
        self._cargo = new_cargo

    @property
    def service(self) -> Service:
        return self._service

    @service.setter
    def service(self, new_service: Service) -> None:
        self._service = new_service

    @property
    def delivery_instructions(self) -> list[str]:
        return self._delivery_instructions

    @delivery_instructions.setter
    def delivery_instructions(self, new_instructions: list[str]):
        self._delivery_instructions = new_instructions

    @property
    def client_name(self) -> str:
        return self._client_name

    @client_name.setter
    def client_name(self, new_name: str) -> None:
        self._client_name = new_name

    @property
    def shipment_dates(self):
        return self._shipment_dates

    @shipment_dates.setter
    def shipment_dates(self, new_dates: ShipmentDates):
        self._shipment_dates = new_dates
