from src.main.freight.address.validation import AddressValidationStrategy


class Address:
    def __init__(self):
        self._name = ""
        self._line_1 = ""
        self._line_2 = ""
        self._line_3 = ""
        self._town = ""
        self._post_code = ""
        self._country = "GB"
        self._telephone_number = ""
        self._contact_name = ""

        self._validation = AddressValidationStrategy()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not self._validation.validate_name(new_name):
            raise ValueError("Requested name is invalid.")

        self._name = new_name

    @property
    def line_1(self):
        return self._line_1

    @line_1.setter
    def line_1(self, new_line):
        if not self._validation.validate_line_1(new_line):
            raise ValueError("Line 1 is invalid.")

        self._line_1 = new_line

    @property
    def line_2(self):
        return self._line_2

    @line_2.setter
    def line_2(self, new_line):
        self._line_2 = new_line

    @property
    def line_3(self):
        return self._line_3

    @line_3.setter
    def line_3(self, new_line):
        self._line_3 = new_line

    @property
    def town(self):
        return self._town

    @town.setter
    def town(self, new_town: str):
        if not self._validation.validate_town(new_town):
            raise ValueError("Town is invalid.")

        self._town = new_town

    @property
    def post_code(self: str):
        return self._post_code

    @post_code.setter
    def post_code(self, new_post_code: str):
        if not self._validation.validate_post_code(new_post_code):
            raise ValueError("Post code is invalid.")

        self._post_code = new_post_code

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, new_contact_name):
        self._contact_name = new_contact_name

    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, new_telephone_number):
        self._telephone_number = new_telephone_number
