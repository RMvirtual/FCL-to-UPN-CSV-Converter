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
        result.barcode = candidate[self._interface.barcode.mapping]

        result.consignment_no = candidate[
            self._interface.consignment_no.mapping]

        result.customer_reference = candidate[
            self._interface.customer_reference.mapping]

        return result

    def unmarshall_depot_no(self, candidate: dict) -> int:
        return candidate[self._interface.depot_no.mapping]

    def unmarshall_customer_id(self, candidate: dict) -> int:
        return candidate[self._interface.customer_id.mapping]

    def unmarshall_delivery_address(self, candidate: dict) -> Address:
        result = Address()
        result.name = self.candidate_from_interface(candidate, "delivery_name")

        result.line_1 = self.candidate_from_interface(
            candidate, "delivery_address_1")

        result.line_2 = self.candidate_from_interface(
            candidate, "delivery_address_2")

        result.town = self.candidate_from_interface(
            candidate, "delivery_town")

        result.county = self.candidate_from_interface(
            candidate, "delivery_county")

        result.post_code = self.candidate_from_interface(
            candidate, "delivery_post_code")

        result.country = self.candidate_from_interface(
            candidate, "delivery_country")

        result.contact_name = self.candidate_from_interface(
            candidate, "delivery_contact_name")

        result.telephone_no = self.candidate_from_interface(
            candidate, "delivery_telephone_no")

        return result

    def candidate_from_interface(self, candidate: dict, field_name) -> any:
        return candidate[self._mapping_from_interface(field_name)]

    def _mapping_from_interface(self, field_name):
        return getattr(self._interface, field_name).mapping
