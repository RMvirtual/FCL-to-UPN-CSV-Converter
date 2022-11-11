import dataclasses


@dataclasses.dataclass
class Address:
    name: str = ""
    line_1: str = ""
    line_2: str = ""
    town: str = ""
    county: str = ""
    post_code: str = ""
    contact_name: str = ""
    telephone_no: str = ""

