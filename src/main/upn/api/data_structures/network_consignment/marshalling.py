from src.main.upn.api.data_structures.network_consignment import mapping
from src.main.upn.consignments.network_consignment.implementation \
    import NetworkConsignment

from src.main.upn.api.data_structures.network_pallet.marshalling \
    import UpnNetworkPalletMarshaller

from src.main.upn.packages.network_pallet.interface \
    import NetworkPalletInterface

from src.main.upn.freight.references.references import UPNReferences
from src.main.upn.freight.address.address import UPNAddress
from src.main.upn.freight.customer.customer import UPNCustomer
from src.main.upn.freight.dates.dates import UPNDates
from src.main.upn.freight.services.services import UPNServices


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._mapping = mapping.network_consignment()
        self._pallet_marshaller = UpnNetworkPalletMarshaller()

    def unmarshall(self, candidate: dict[str, any]) -> NetworkConsignment:
        result = NetworkConsignment()
        result.references = self.unmarshall_references(candidate)

        return result

    def unmarshall_references(
            self, candidate: dict[str, any]) -> UPNReferences:
        result = UPNReferences()
        result.barcode = self._unmarshall(candidate, "barcode")
        result.consignment_no = self._unmarshall(candidate, "consignment_no")

        result.customer_reference = self._unmarshall(
            candidate, "customer_reference")

        return result

    def unmarshall_depot_no(self, candidate: dict[str, any]) -> int:
        return self._unmarshall(candidate, "depot_no")

    def unmarshall_customer(self, candidate: dict[str, any]) -> UPNCustomer:
        result = UPNCustomer()
        result.name = self._unmarshall(candidate, "customer_name")
        result.id = self._unmarshall(candidate, "customer_id")

        return result

    def unmarshall_delivery_address(
            self, candidate: dict[str, any]) -> UPNAddress:
        def _unmarshall_candidate(field_name) -> any:
            return self._unmarshall(candidate, field_name)

        result = UPNAddress()
        result.name = _unmarshall_candidate("delivery_name")
        result.line_1 = _unmarshall_candidate("delivery_address_1")
        result.line_2 = _unmarshall_candidate("delivery_address_2")
        result.town = _unmarshall_candidate("delivery_town")
        result.county = _unmarshall_candidate("delivery_county")
        result.post_code = _unmarshall_candidate("delivery_post_code")
        result.country = _unmarshall_candidate("delivery_country")
        result.contact_name = _unmarshall_candidate("delivery_contact_name")
        result.telephone_no = _unmarshall_candidate("delivery_telephone_no")

        return result

    def unmarshall_total_weight(self, candidate: dict[str, any]) -> int:
        return self._unmarshall(candidate, "total_weight")

    def unmarshall_special_instructions(
            self, candidate: dict[str, any]) -> str:
        return self._unmarshall(candidate, "special_instructions")

    def unmarshall_customer_paperwork_pages(
            self, candidate: dict[str, any]) -> int:
        return self._unmarshall(candidate, "customer_paperwork_pages")

    def unmarshall_dates(self, candidate: dict[str, any]) -> UPNDates:
        result = UPNDates()
        result.despatch = self._unmarshall(candidate, "despatch_date")
        result.delivery = self._unmarshall(candidate, "delivery_datetime")

        return result

    def unmarshall_services(self, candidate: dict[str, any]) -> UPNServices:
        result = UPNServices()
        result.main_service = self._unmarshall(candidate, "main_service")
        result.premium_service = self._unmarshall(candidate, "premium_service")

        result.tail_lift_required = self._unmarshall(
            candidate, "tail_lift_required")

        result.additional_service = self._unmarshall(
            candidate, "additional_service")

        return result

    def unmarshall_pallets(
            self, candidate: dict[str, any]) -> list[NetworkPalletInterface]:
        pallets = self._unmarshall(candidate, "pallets")["NetworkPallet"]

        return list(map(self._pallet_marshaller.unmarshall, pallets))

    def _unmarshall(self, candidate: dict[str, any], field_name: str) -> any:
        return candidate[self._map_interface_to(field_name)]

    def _map_interface_to(self, field_name: str):
        return getattr(self._mapping, field_name).mapping
