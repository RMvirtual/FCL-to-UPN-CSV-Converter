from src.main.consignment.address import Address
from src.main.consignment.reference import Reference


class Consignment:
    def __init__(self):
        self._reference: Reference or None = None
        self._shipper_reference: str = ""
        self._consignee_reference: str = ""
        self._client_name: str = ""
        self._address: Address = Address()
        self._delivery_instructions = ""
        # N/D or Std
        # AM/Pre-10AM/Timed/Saturday AM
        # Tail lift
        # Book-In/Booked
        # Goods description

    @property
    def reference(self) -> str:
        return None if self._reference is None else str(self._reference)

    @reference.setter
    def reference(self, new_reference: str) -> None:
        try:
            self._reference = Reference(new_reference)

        except ValueError as error:
            raise error

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, new_address: Address) -> None:
        self._address = new_address

