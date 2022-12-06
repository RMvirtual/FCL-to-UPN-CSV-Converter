from src.main.companies.upn.interfaces.api.network_consignment.keys \
    import NetworkConsignmentKeyMap

from src.main.file_system.companies.upn import api


class NetworkConsignmentKeys(NetworkConsignmentKeyMap):
    def __init__(self):
        self._keys = api.network_consignment_keys()

    @property
    def consignment_no(self) -> str:
        return self._keys["consignment_no"]

    @property
    def barcode(self) -> str:
        return self._keys["barcode"]

    @property
    def customer_reference(self) -> str:
        return self._keys["customer_reference"]

    @property
    def depot_no(self) -> str:
        return self._keys["depot_no"]

    @property
    def despatch_date(self) -> str:
        return self._keys["despatch_date"]

    @property
    def delivery_datetime(self) -> str:
        return self._keys["delivery_datetime"]

    @property
    def delivery_name(self) -> str:
        return self._keys["delivery_name"]

    @property
    def delivery_address_1(self) -> str:
        return self._keys["delivery_address_1"]

    @property
    def delivery_address_2(self) -> str:
        return self._keys["delivery_address_2"]

    @property
    def delivery_town(self) -> str:
        return self._keys["delivery_town"]

    @property
    def delivery_county(self) -> str:
        return self._keys["delivery_county"]

    @property
    def delivery_post_code(self) -> str:
        return self._keys["delivery_post_code"]

    @property
    def delivery_country(self) -> str:
        return self._keys["delivery_country"]

    @property
    def delivery_contact_name(self) -> str:
        return self._keys["delivery_contact_name"]

    @property
    def delivery_telephone_no(self) -> str:
        return self._keys["delivery_telephone_no"]

    @property
    def total_weight(self) -> str:
        return self._keys["total_weight"]

    @property
    def special_instructions(self) -> str:
        return self._keys["special_instructions"]

    @property
    def customer_id(self) -> str:
        return self._keys["customer_id"]

    @property
    def customer_name(self) -> str:
        return self._keys["customer_name"]

    @property
    def customer_paperwork_pages(self) -> str:
        return self._keys["customer_paperwork_pages"]

    @property
    def main_service(self) -> str:
        return self._keys["main_service"]

    @property
    def premium_service(self) -> str:
        return self._keys["premium_service"]

    @property
    def tail_lift_required(self) -> str:
        return self._keys["tail_lift_required"]

    @property
    def additional_service(self) -> str:
        return self._keys["additional_service"]

    @property
    def pallets(self) -> str:
        return self._keys["pallets"]
