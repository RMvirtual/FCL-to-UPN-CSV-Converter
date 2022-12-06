from src.main.companies.upn.api.mapping import network_consignment
from src.main.companies.upn.api.marshalling import customer
from src.main.companies.upn.api.marshalling import references
from src.main.companies.upn.api.marshalling import services
from src.main.companies.upn.api.marshalling import delivery_address
from src.main.companies.upn.api.marshalling.network_pallet \
    import UpnNetworkPalletMarshaller
from src.main.companies.upn.implementations.network_consignment \
    .implementation import NetworkConsignment
from src.main.companies.upn.implementations.services.container \
    import ServicesProvider
from src.main.companies.upn.implementations.time.dates import UPNDates
from src.main.companies.upn.interfaces.address import UPNAddressable
from src.main.companies.upn.interfaces.consignments import ConsignmentDownload
from src.main.companies.upn.interfaces.customer import CustomerDetails
from src.main.companies.upn.interfaces.pallets import NetworkPallet

UPNDict = dict[str, any]


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._mapping = network_consignment.mapping()
        self._pallet_marshaller = UpnNetworkPalletMarshaller()

    def unmarshall(self, candidate: UPNDict) -> ConsignmentDownload:
        result = NetworkConsignment()
        result.references = references.unmarshall_references(candidate)

        return result

    def unmarshall_depot_no(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "depot_no")

    def unmarshall_customer(self, candidate: UPNDict) -> CustomerDetails:
        return customer.unmarshall(candidate)

    def unmarshall_del_address(self, candidate: UPNDict) -> UPNAddressable:
        return delivery_address.unmarshall(candidate)

    def unmarshall_total_weight(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "total_weight")

    def unmarshall_special_instructions(self, candidate: UPNDict) -> str:
        return self._unmarshall(candidate, "special_instructions")

    def unmarshall_customer_paperwork_pages(self, candidate: UPNDict) -> int:
        return self._unmarshall(candidate, "customer_paperwork_pages")

    def unmarshall_dates(self, candidate: UPNDict) -> UPNDates:
        result = UPNDates()
        result.despatch = self._unmarshall(candidate, "despatch_date")
        result.delivery = self._unmarshall(candidate, "delivery_datetime")

        return result

    def unmarshall_services(self, candidate: UPNDict) -> ServicesProvider:
        return services.unmarshall(candidate)

    def unmarshall_pallets(self, candidate: UPNDict) -> list[NetworkPallet]:
        pallets = self._unmarshall(candidate, "pallets")["NetworkPallet"]

        return list(map(self._pallet_marshaller.unmarshall, pallets))

    def _unmarshall(self, candidate: UPNDict, field_name: str) -> any:
        return candidate[self._map_interface_to(field_name)]

    def _map_interface_to(self, field_name: str):
        return getattr(self._mapping, field_name).mapping
