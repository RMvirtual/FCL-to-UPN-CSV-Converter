import dataclasses
import re


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
        self._initialise_uk_post_code_pattern()

    def _initialise_uk_post_code_pattern(self):
        self._uk_post_code_pattern = re.compile(
            r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})"
            + r"|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})"
            + r"|(([A-Za-z][0-9][A-Za-z])"
            + r"|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
        )

    def validate_name(self, name: str) -> bool:
        return bool(name)

    def validate_line(self, line: str) -> bool:
        return bool(line)

    def validate_town(self, town: str) -> bool:
        return bool(town)

    def validate_post_code(self, post_code: str) -> bool:
        return self._post_code_pattern_matches(post_code)

    def _post_code_pattern_matches(self, post_code: str) -> bool:
        return bool(self._uk_post_code_pattern.fullmatch(post_code))
