import dataclasses


@dataclasses.dataclass
class AddressParseRequest:
    name: str = ""
    line_1: str = ""
    line_2: str = ""
    line_3: str = ""
    town: str = ""
    post_code: str = ""
    country: str = "GB"
    contact_name: str = ""
    telephone_number: str = ""


@dataclasses.dataclass
class ServiceParseRequest:
    priority_code: str = ""
    tail_lift_requested: bool = False


@dataclasses.dataclass
class CargoEntryParseRequest:
    quantity: int = 0
    package_type: str = ""
    weight: float = 0
    goods_description: str = ""


@dataclasses.dataclass
class CargoParseRequest:
    line_1: CargoEntryParseRequest = None
    line_2: CargoEntryParseRequest = None
    line_3: CargoEntryParseRequest = None
    line_4: CargoEntryParseRequest = None

