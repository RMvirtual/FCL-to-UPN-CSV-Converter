import dataclasses


@dataclasses.dataclass
class Mapping:
    type: str = ""
    mapping: str = ""
    values: list[any] = None


