import copy
from src.main.addresses.interface import Address
from src.main.companies.upn.interfaces.address import UPNAddressable


class UPNAddressAdaptor(Address):
    """Class for adapting a UPN address structure into a system
    address.
    """
    def __init__(self, upn_address: UPNAddressable):
        self._address = copy.deepcopy(upn_address)

    @property
    def name(self) -> str:
        return self._address.name

    @name.setter
    def name(self, new_name: str) -> None:
        self._address.name = new_name

    @property
    def lines(self) -> list[str]:
        return [
            self._address.line_1,
            self._address.line_2,
            self._address.county
        ]

    @property
    def town(self) -> str:
        return self._address.town

    @town.setter
    def town(self, new_town: str) -> None:
        self._address.town = new_town

    @property
    def post_code(self) -> str:
        return self._address.post_code

    @post_code.setter
    def post_code(self, new_post_code: str) -> None:
        self._address.post_code = new_post_code

    @property
    def country(self) -> str:
        return self._address.country

    @country.setter
    def country(self, new_country: str) -> None:
        self._address.country = new_country

    @property
    def contact_name(self) -> str:
        return self._address.contact_name

    @contact_name.setter
    def contact_name(self, new_contact_name: str) -> None:
        self._address.contact_name = new_contact_name

    @property
    def telephone_number(self) -> str:
        return self._address.telephone_no

    @telephone_number.setter
    def telephone_number(self, new_telephone_number: str) -> None:
        self._address.telephone_no = new_telephone_number
