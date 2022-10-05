import copy

import dataclasses
import re

from src.main.forward_office.dashboard.parser.requests.types \
    import AddressParseRequest


@dataclasses.dataclass
class AddressErrors:
    name_is_blank: bool = False
    line_1_is_blank: bool = False
    town_is_blank: bool = False
    post_code_is_blank: bool = False
    post_code_is_invalid: bool = False

    def __bool__(self):
        return True in dataclasses.fields(self)


class AddressValidationStrategy:
    def __init__(self):
        self._errors = AddressErrors()
        self._initialise_uk_post_code_pattern()

    def _initialise_uk_post_code_pattern(self):
        self._uk_post_code_pattern = re.compile(
            r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})"
            + r"|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})"
            + r"|(([A-Za-z][0-9][A-Za-z])"
            + r"|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
        )

    def validate(self, request: AddressParseRequest) -> AddressErrors:
        self._errors = AddressErrors()

        self._errors.name_is_blank = not request.name
        self._errors.line_1_is_blank = not request.line_1
        self._errors.town_is_blank = not request.town
        self._errors.post_code_is_blank = not request.post_code

        self._errors.post_code_is_invalid = (
            self._validate_post_code(request.post_code)
            or self._errors.post_code_is_blank
        )

        return copy.copy(self._errors)

    def _validate_post_code(self, post_code: str):
        return bool(self._uk_post_code_pattern.fullmatch(post_code))





