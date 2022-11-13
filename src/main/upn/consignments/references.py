import dataclasses


@dataclasses.dataclass
class References:
    barcode_no: str = ""
    consignment_no: str = ""
    customer_reference: str = ""

