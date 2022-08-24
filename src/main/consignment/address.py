

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

    def is_valid(self):
        return (
            self._name != ""
            and self._line_1 != ""
            and self._town != ""
            and self._post_code != ""
            and self._country != ""
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def line_1(self):
        return self._line_1

    @line_1.setter
    def line_1(self, new_line):
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
    def town(self, new_town):
        self._town = new_town

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, new_post_code):
        self._post_code = new_post_code

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, new_telephone_number):
        self._telephone_number = new_telephone_number
