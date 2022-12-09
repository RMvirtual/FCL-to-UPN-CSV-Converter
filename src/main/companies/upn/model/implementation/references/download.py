from src.main.companies.upn.api.interface.references.download \
    import ReferencesDownload

from src.main.companies.upn.model.implementation.references.upload \
    import UPNReferenceUpload


class UPNReferences(ReferencesDownload, UPNReferenceUpload):
    def __init__(self, consignment_no: str, customer_ref: str, barcode: str):
        super().__init__(consignment_no, customer_ref)
        self._barcode = barcode

    @property
    def barcode(self) -> str:
        return self._barcode
