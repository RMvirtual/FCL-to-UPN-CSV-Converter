from src.main.freight.address.model import Address
from src.main.freight.reference.model import Reference
from src.main.freight.cargo.model import Cargo
from src.main.freight.service.model import Service
from src.main.freight.shipment_dates.model import ShipmentDates


class Consignment:
    def __init__(self):
        self._reference: Reference or None = None
        self._shipper_reference: str = ""
        self._consignee_reference: str = ""
        self._client_name: str = ""
        self._address: Address = Address()
        self._cargo = Cargo()
        self._service = Service()
        self._shipment_dates = ShipmentDates()
        self._delivery_instructions: list[str] = []

    @property
    def reference(self) -> str:
        return None if self._reference is None else str(self._reference)

    @reference.setter
    def reference(self, new_reference: str or Reference) -> None:
        if type(new_reference) is Reference:
            self._reference = new_reference

        elif type(new_reference) is str:
            self._reference = Reference(new_reference)

        else:
            raise TypeError("Incorrect input type for a reference.")

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, new_address: Address) -> None:
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
