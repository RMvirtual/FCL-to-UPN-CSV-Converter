import copy
from src.main.upn.api.data_structures.network_consignment import interface
import datetime


class NetworkConsignment:
    def __init__(self):
        self._interface = interface.NetworkConsignmentInterface()
        self._consignment_no = ""
        self._depot_no = 75
        self._customer_reference = ""
        self._despatch_date = None
        self._delivery_name = ""
        self._delivery_address_1 = ""
        self._delivery_address_2 = ""
        self._delivery_town = ""
        self._delivery_county = ""
        self._delivery_post_code = ""
        self._delivery_telephone_no = ""
        self._total_weight = 0
        self._special_instructions = ""
        self._customer_id = 0
        self._delivery_contact_name = ""
        self._delivery_country = ""
        self._customer_paperwork_pages = 0
        self._main_service = ""
        self._premium_service = ""
        self._tail_lift_required = ""
        self._additional_service = ""
        self._delivery_datetime = None
        self._consignment_barcode = ""
        self._pallets = []

