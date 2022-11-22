import dataclasses


@dataclasses.dataclass
class UPNReferences:
    consignment_no: str = ""
    barcode: str = ""
    customer_reference: str = ""
