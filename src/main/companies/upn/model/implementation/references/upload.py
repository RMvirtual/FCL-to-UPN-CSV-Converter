from src.main.companies.upn.api.interface.references.upload \
    import ReferencesUpload


class UPNReferenceUpload(ReferencesUpload):
    def __init__(self, consignment_no: str, customer_ref: str):
        self._consignment_no = consignment_no
        self._customer_ref = customer_ref

    @property
    def consignment_no(self) -> str:
        return self._consignment_no

    @property
    def customer_reference(self) -> str:
        return self._customer_ref
