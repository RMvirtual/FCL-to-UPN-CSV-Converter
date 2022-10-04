from src.main.freight.consignment.address import Address
from src.main.freight.consignment.reference import Reference
from src.main.freight.cargo.model import Cargo
from src.main.freight.service.model import Service


class Consignment:
    def __init__(self):
        self._reference: Reference or None = None
        self._shipper_reference: str = ""
        self._consignee_reference: str = ""
        self._client_name: str = ""
        self._address: Address = Address()
        self._cargo = Cargo()
        self._service = Service()
        self._delivery_instructions = ""

    @property
    def reference(self) -> str:
        return None if self._reference is None else str(self._reference)

    @reference.setter
    def reference(self, new_reference: str or Reference) -> None:
        if type(new_reference) is Reference:
            self._reference = new_reference

        elif type(new_reference) is str:
            try:
                self._reference = Reference(new_reference)

            except ValueError as error:
                raise error

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
