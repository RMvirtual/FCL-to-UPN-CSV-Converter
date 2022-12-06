from src.main.companies.upn.interfaces.api.references import ReferencesDownload


class UPNReferences(ReferencesDownload):
    def __init__(self, consignment_no: str, customer_ref: str, barcode: str):
        self._consignment_no = consignment_no
        self._customer_ref = customer_ref
        self._barcode = barcode

    @property
    def consignment_no(self) -> str:
        return self._consignment_no

    @property
    def customer_reference(self) -> str:
        return self._customer_ref

    @property
    def barcode(self) -> str:
        return self._barcode
