import dataclasses


@dataclasses.dataclass
class UPNAddress:
    name: str = ""
    line_1: str = ""
    line_2: str = ""
    town: str = ""
    county: str = ""
    post_code: str = ""
    country: str = ""
    contact_name: str = ""
    telephone_no: str = ""
