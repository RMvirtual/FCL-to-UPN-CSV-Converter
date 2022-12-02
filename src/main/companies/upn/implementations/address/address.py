from src.main.addresses.implementation import Address
from src.main.companies.upn.interfaces.address import UPNAddressable


class UPNAddress(UPNAddressable):
    def __init__(self):
        self._address = Address()

    @property
    def name(self) -> str:
        return self._address.name

    @property
    def line_1(self) -> str:
        return self._address.lines[0] if len(self._address) > 0 else ""

    @property
    def line_2(self) -> str:
        return self._address.lines[1] if len(self._address) > 1 else ""

    @property
    def town(self) -> str:
        return self._address.town

    @property
    def county(self) -> str:
        return self._address.lines[2] if len(self._address) > 2 else ""

    @property
    def post_code(self) -> str:
        return self._address.post_code

    @property
    def country(self) -> str:
        return self._address.country

    @property
    def contact_name(self) -> str:
        return self._address.contact_name

    @property
    def telephone_no(self) -> str:
        return self._address.telephone_number

    @name.setter
    def name(self, new_name: str) -> None:
        self._address.name = new_name

    @line_1.setter
    def line_1(self, new_line: str) -> None:
        self._address.lines[0] = new_line

    @line_2.setter
    def line_2(self, new_line: str) -> None:
        self._address.lines[1] = new_line

    @town.setter
    def town(self, new_town: str) -> None:
        self._address.town = new_town

    @county.setter
    def county(self, new_county: str) -> None:
        self._address.lines[2] = new_county

    @post_code.setter
    def post_code(self, new_post_code: str) -> None:
        self._address.post_code = new_post_code

    @country.setter
    def country(self, new_country: str) -> None:
        self._address.country = new_country

    @contact_name.setter
    def contact_name(self, new_contact_name: str) -> None:
        self._address.contact_name = new_contact_name

    @telephone_no.setter
    def telephone_no(self, new_number: str) -> None:
        self._address.telephone_number = new_number
