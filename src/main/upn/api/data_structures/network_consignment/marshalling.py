from src.main.upn.api.data_structures.network_consignment import interface

from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.consignments.references import References
from src.main.upn.consignments.address import Address
from src.main.upn.consignments.cargo import Cargo
from src.main.upn.consignments.customer import Customer
from src.main.upn.consignments.dates import Dates
from src.main.upn.consignments.services import Services

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

    def unmarshall_customer(self, candidate: dict) -> int:
        result = Customer()
        result.name = self._unmarshall(candidate, "customer_name")
        result.id = self._unmarshall(candidate, "customer_id")

        return result

    def unmarshall_delivery_address(self, candidate: dict) -> Address:
        def _unmarshall_candidate(field_name) -> any:
            return self._unmarshall(candidate, field_name)

        result = Address()
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

    def unmarshall_total_weight(self, candidate: dict) -> int:
        return self._unmarshall(candidate, "total_weight")

    def unmarshall_special_instructions(self, candidate: dict) -> str:
        return self._unmarshall(candidate, "special_instructions")

    def unmarshall_customer_paperwork_pages(self, candidate: dict) -> int:
        return self._unmarshall(candidate, "customer_paperwork_pages")

    def unmarshall_dates(self, candidate) -> Dates:
        result = Dates()
        result.despatch = self._unmarshall(candidate, "despatch_date")
        result.delivery = self._unmarshall(candidate, "delivery_datetime")

        return result

    def unmarshall_services(self, candidate) -> Services:
        result = Services()

        return result

    def _unmarshall(self, candidate: dict, field_name) -> any:
        return candidate[self._interface_mapping_from(field_name)]

    def _interface_mapping_from(self, field_name):
        return getattr(self._interface, field_name).mapping
