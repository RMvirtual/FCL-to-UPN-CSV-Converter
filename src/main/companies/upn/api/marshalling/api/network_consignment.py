from src.main.companies.upn.model.implementation.consignment.download\
    .implementation import NetworkConsignment
from src.main.companies.upn.model.implementation.service.container \
    import ServicesProvider
from src.main.companies.upn.api.interface.consignment.download \
    import ConsignmentDownload
from src.main.companies.upn.api.interface.dates.dates import DatesProvider
from src.main.companies.upn.api.interface.cargo.pallets.download \
    import DownloadPallet
from src.main.companies.upn.api.interface.database.address.generic \
    import UPNAddressable
from src.main.companies.upn.api.interface.database.customer.customer \
    import CustomerDetails
from src.main.companies.upn.api.constraints import network_consignment
from src.main.companies.upn.api.marshalling.api.dates \
    import UPNDatesUnmarshaller
from src.main.companies.upn.api.marshalling.api.network_pallet \
    import UpnNetworkPalletMarshaller
from src.main.companies.upn.api.marshalling.api.references \
    import UPNReferencesUnmarshaller
from src.main.companies.upn.api.marshalling.database.customer \
    import UPNCustomerUnmarshaller
from src.main.companies.upn.api.marshalling.database.services \
    import UPNServicesUnmarshaller
from src.main.companies.upn.api.marshalling.database.delivery_address \
    import UPNDeliveryAddressUnmarshaller

UPNDict = dict[str, any]


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._mapping = network_consignment.constraints()
        self._pallet_marshaller = UpnNetworkPalletMarshaller()

    def unmarshall(self, candidate: UPNDict) -> ConsignmentDownload:
        result = NetworkConsignment()

        return result

    def unmarshall_references(self, candidate: UPNDict) -> any:
        marshaller = UPNReferencesUnmarshaller()

        return marshaller.references(candidate)

    def unmarshall_depot_no(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "depot_no")

    def unmarshall_customer(self, candidate: UPNDict) -> CustomerDetails:
        marshaller = UPNCustomerUnmarshaller()

        return marshaller.customer(candidate)

    def unmarshall_del_address(self, candidate: UPNDict) -> UPNAddressable:
        marshaller = UPNDeliveryAddressUnmarshaller()

        return marshaller.delivery_address(candidate)

    def unmarshall_total_weight(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "total_weight")

    def unmarshall_special_instructions(self, candidate: UPNDict) -> str:
        return self._unmarshall(candidate, "special_instructions")

    def unmarshall_customer_paperwork_pages(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "customer_paperwork_pages")

    def unmarshall_dates(self, candidate: UPNDict) -> DatesProvider:
        marshaller = UPNDatesUnmarshaller()

        return marshaller.dates(candidate)

    def unmarshall_services(self, candidate: UPNDict) -> ServicesProvider:
        marshaller = UPNServicesUnmarshaller()

        return marshaller.services(candidate)

    def unmarshall_pallets(self, candidate: UPNDict) -> list[DownloadPallet]:
        pallets = self._unmarshall(candidate, "pallets")["NetworkPallet"]

        return list(map(self._pallet_marshaller.unmarshall, pallets))

    def _unmarshall(self, candidate: UPNDict, field_name: str) -> any:
        return candidate[self._map_interface_to(field_name)]

    def _map_interface_to(self, field_name: str):
        return getattr(self._mapping, field_name).constraints
