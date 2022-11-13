from src.main.upn.api.data_structures.network_consignment import interface

from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.consignments.references import References
from src.main.upn.consignments.address import Address


class UpnNetworkConsignmentMarshaller:
    def __init__(self):
        self._interface = interface.network_consignment()

    def unmarshall(self, candidate: dict) -> NetworkConsignment:
        result = NetworkConsignment()
        result.references = self.unmarshall_references(candidate)

        return result

    def unmarshall_references(self, candidate: dict) -> References:
        result = References()
        result.barcode = self._unmarshall(candidate, "barcode")
        result.consignment_no = self._unmarshall(candidate, "consignment_no")

        result.customer_reference = self._unmarshall(
            candidate, "customer_reference")

        return result

    def unmarshall_depot_no(self, candidate: dict) -> int:
        return self._unmarshall(candidate, "depot_no")

    def unmarshall_customer_id(self, candidate: dict) -> int:
        return self._unmarshall(candidate, "customer_id")

    def unmarshall_delivery_address(self, candidate: dict) -> Address:
        result = Address()
        result.name = self._unmarshall(candidate, "delivery_name")
        result.line_1 = self._unmarshall(candidate, "delivery_address_1")
        result.line_2 = self._unmarshall(candidate, "delivery_address_2")
        result.town = self._unmarshall(candidate, "delivery_town")
        result.county = self._unmarshall(candidate, "delivery_county")
        result.post_code = self._unmarshall(candidate, "delivery_post_code")
        result.country = self._unmarshall(candidate, "delivery_country")

        result.contact_name = self._unmarshall(
            candidate, "delivery_contact_name")

        result.telephone_no = self._unmarshall(
            candidate, "delivery_telephone_no")

        return result

    def _unmarshall(self, candidate: dict, field_name) -> any:
        return candidate[self._interface_mapping_from(field_name)]

    def _interface_mapping_from(self, field_name):
        return getattr(self._interface, field_name).mapping
