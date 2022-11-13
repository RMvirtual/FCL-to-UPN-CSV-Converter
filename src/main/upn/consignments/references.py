import dataclasses


@dataclasses.dataclass
class References:
    consignment_no: str = ""
    barcode: str = ""
    customer_reference: str = ""
