from src.main.companies.upn.api.marshalling.unmarshaller \
    import UPNAPIUnmarshaller
from src.main.companies.upn.implementations.references.references \
    import UPNReferences
from src.main.companies.upn.interfaces.references import ReferencesDownload


class UPNReferencesUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def references(self, candidate: dict[str, any]) -> ReferencesDownload:
        return UPNReferences(
            barcode=self.unmarshall(candidate, "barcode"),
            consignment_no=self.unmarshall(candidate, "consignment_no"),
            customer_ref=self.unmarshall(candidate, "customer_reference")
        )
