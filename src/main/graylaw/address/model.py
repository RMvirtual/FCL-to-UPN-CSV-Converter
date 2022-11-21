from src.main.graylaw.address import interface
from src.main.graylaw.address.validation import AddressValidationStrategy


class Address(interface.Address):
    def __init__(self):
        self._name = ""
        self._lines: list[str] = []
        self._town = ""
        self._post_code = ""
        self._country = "GB"
        self._telephone_number = ""
        self._contact_name = ""
        self._validation = AddressValidationStrategy()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not self._validation.validate_name(new_name):
            raise ValueError("Requested name is invalid.")

        self._name = new_name

    @property
    def lines(self) -> list[str]:
        return self._lines

    @property
    def town(self) -> str:
        return self._town

    @town.setter
    def town(self, new_town: str) -> None:
        if not self._validation.validate_town(new_town):
            raise ValueError("Town is invalid.")

        self._town = new_town

    @property
    def post_code(self) -> str:
        return self._post_code

    @post_code.setter
    def post_code(self, new_post_code: str) -> None:
        if not self._validation.validate_post_code(new_post_code):
            raise ValueError("Post code is invalid.")

        self._post_code = new_post_code

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, new_country) -> None:
        self._country = new_country

    @property
    def contact_name(self) -> str:
        return self._contact_name

    @contact_name.setter
    def contact_name(self, new_contact_name: str) -> None:
        self._contact_name = new_contact_name

    @property
    def telephone_number(self) -> str:
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, new_telephone_number: str) -> None:
        self._telephone_number = new_telephone_number
