import dataclasses


@dataclasses.dataclass
class DatesAsIntegers:
    day: int = 0
    month: int = 0
    year: int = 0

    def pad_year(self) -> None:
        self.year = int("20" + str(self.year)) \
            if len(str(self.year)) == 2 else self.year


@dataclasses.dataclass
class DatesAsStrings:
    day: str = ""
    month: str = ""
    year: str = ""

    def to_integers(self) -> DatesAsIntegers:
        result = DatesAsIntegers()

        result.day = int(self.day)
        result.month = int(self.month)
        result.year = int(self.year)

        return result
