from src.main.addresses.implementation import Address
from src.main.companies.upn.api.interface_1.database.address.generic import UPNAddressable


class UPNAddress(UPNAddressable):
    def __init__(self):
        self._address = Address()

    @property
    def name(self) -> str:
        return self._address.name

    @property
    def line_1(self) -> str:
        return self._get_line(0)

    @property
    def line_2(self) -> str:
        return self._get_line(1)

    @property
    def town(self) -> str:
        return self._address.town

    @property
    def county(self) -> str:
        return self._get_line(2)

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
        self._set_line(line_no=0, line_value=new_line)

    @line_2.setter
    def line_2(self, new_line: str) -> None:
        self._set_line(line_no=1, line_value=new_line)

    @town.setter
    def town(self, new_town: str) -> None:
        self._address.town = new_town

    @county.setter
    def county(self, new_county: str) -> None:
        self._set_line(line_no=2, line_value=new_county)

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

    def _set_line(self, line_no: int, line_value: str) -> None:
        if self._has_line(line_no):
            self._address.lines[line_no] = line_value

        else:
            self._address.lines.append(line_value)

    def _get_line(self, line_no: int) -> str:
        return (
            self._address.lines[line_no] if self._has_line(line_no) else "")

    def _has_line(self, line_no) -> bool:
        return len(self._address.lines) > line_no

