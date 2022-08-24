

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
