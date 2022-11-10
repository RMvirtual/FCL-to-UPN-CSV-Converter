from src.main.upn.api.data_structures.network_consignment.structure \
    import NetworkConsignment

from src.main.upn.api.data_structures.network_consignment.mapping \
    import NetworkConsignmentStructure


class NetworkConsignmentParser:
    def __init__(self):
        self._structure = NetworkConsignmentStructure()
        self._consignment = NetworkConsignment()

    def consignment_barcode_no(self, parse_values: dict):
        return parse_values[self._structure.consignment_barcode_no.mapping]

    def consignment_no(self, parse_values: dict):
        return parse_values[self._structure.consignment_no.mapping]

    def customer_name(self, parse_values: dict):
        return parse_values[self._structure.customer_name.mapping]

    def customer_id(self, parse_values: dict):
        return parse_values[self._structure.customer_id.mapping]

    def depot_no(self, parse_values: dict):
        return parse_values[self._structure.depot_no.mapping]

    def despatch_date(self, parse_values: dict):
        return parse_values[self._structure.despatch_date.mapping]

    def delivery_name(self, parse_values: dict):
        return parse_values[self._structure.delivery_name.mapping]

    def delivery_address_1(self, parse_values: dict):
        return parse_values[self._structure.delivery_address_1.mapping]

    def delivery_address_2(self, parse_values: dict):
        return parse_values[self._structure.delivery_address_2.mapping]

    def delivery_town(self, parse_values: dict):
        return parse_values[self._structure.delivery_town.mapping]

    def delivery_county(self, parse_values: dict):
        return parse_values[self._structure.delivery_county.mapping]

    def delivery_post_code(self, parse_values: dict):
        return parse_values[self._structure.delivery_post_code.mapping]

    def delivery_telephone_no(self, parse_values: dict):
        return parse_values[self._structure.delivery_telephone_no.mapping]

    def total_weight(self, parse_values: dict):
        return parse_values[self._structure.total_weight.mapping]

    def special_instructions(self, parse_values: dict):
        return parse_values[self._structure.special_instructions.mapping]

    def delivery_contact_name(self, parse_values: dict):
        return parse_values[self._structure.delivery_contact_name.mapping]

    def delivery_country(self, parse_values: dict):
        return parse_values[self._structure.delivery_country.mapping]

    def customer_paperwork_pages(self, parse_values: dict):
        return parse_values[self._structure.customer_paperwork_pages.mapping]

    def main_service(self, parse_values: dict):
        return parse_values[self._structure.main_service.mapping]

    def premium_service(self, parse_values: dict):
        return parse_values[self._structure.premium_service.mapping]

    def tail_lift_required(self, parse_values: dict):
        return parse_values[self._structure.tail_lift_required.mapping]

    def additional_service(self, parse_values: dict):
        return parse_values[self._structure.additional_service.mapping]

    def delivery_datetime(self, parse_values: dict):
        return parse_values[self._structure.delivery_datetime.mapping]

    def pallets(self, parse_values: dict):
        return None
