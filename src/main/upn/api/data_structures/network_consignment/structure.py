import copy
from src.main.upn.api.data_structures.network_consignment import interface
import datetime
from src.main.upn.consignments.address import Address
from src.main.upn.consignments.references import References
from src.main.upn.consignments.services import Services


class NetworkConsignment:
    def __init__(self):
        self._interface = interface.NetworkConsignmentInterface()
        self._customer_id = 0
        self._depot_no = 75
        self._delivery_address = Address()
        self._references = References()
        self._services = Services()
        self._special_instructions = ""
        self._pallets = []
        self._total_weight = 0
        self._customer_paperwork_pages = 0
        self._despatch_date = None
        self._delivery_datetime = None

    @property
    def delivery_address(self) -> Address:
        return self._delivery_address

    @property
    def references(self) -> References:
        return self._references

    @property
    def services(self) -> Services:
        return self._services

    @property
    def customer_id(self) -> int:
        return self._customer_id

    @customer_id.setter
    def customer_id(self, new_id: int) -> None:
        self._customer_id = new_id

    @property
    def depot_no(self) -> int:
        return self._depot_no

    @depot_no.setter
    def depot_no(self, new_depot_no: int) -> None:
        self._depot_no = new_depot_no

    @property
    def special_instructions(self) -> str:
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, new_instructions: str) -> None:
        self._special_instructions = new_instructions

    @property
    def customer_paperwork_pages(self) -> int:
        return self._customer_paperwork_pages

    @customer_paperwork_pages.setter
    def customer_paperwork_pages(self, new_quantity: int) -> None:
        self._customer_paperwork_pages = new_quantity


