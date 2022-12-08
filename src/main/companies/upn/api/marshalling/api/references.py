from src.main.companies.upn.api.marshalling.controller.unmarshaller \
    import UPNAPIUnmarshaller
from src.main.companies.upn.api.implementation_1.api.references.references \
    import UPNReferences
from src.main.companies.upn.api.interface.references.download \
    import ReferencesDownload


class UPNReferencesUnmarshaller(UPNAPIUnmarshaller):
    def __init__(self):
        super().__init__()

    def references(self, candidate: dict[str, any]) -> ReferencesDownload:
        return UPNReferences(
            barcode=self.unmarshall(candidate, "barcode"),
            consignment_no=self.unmarshall(candidate, "consignment_no"),
            customer_ref=self.unmarshall(candidate, "customer_reference")
        )
