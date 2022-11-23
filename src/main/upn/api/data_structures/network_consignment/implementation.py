import datetime
from src.main.upn.api.data_structures.network_consignment import mapping
from src.main.upn.consignment.structures.address import UPNAddress
from src.main.upn.consignment.structures.references import UPNReferences
from src.main.upn.consignment.structures.services import UPNServices
from src.main.upn.consignment.structures.cargo.container.container import UPNCargo
from src.main.upn.consignment.structures.customer import UPNCustomer
from src.main.upn.consignment.structures.dates import UPNDates
from src.main.upn.api.data_structures.network_consignment import interface

from src.main.upn.api.data_structures.network_consignment.interface \
    import NetworkPallet


class NetworkConsignment(interface.NetworkConsignment):
    def __init__(self):
        self._mappings = mapping.network_consignment()
        self._references = UPNReferences()
        self._depot_no = 75
        self._customer_paperwork_pages = 0
        self._customer = UPNCustomer()
        self._delivery_address = UPNAddress()
        self._dates = UPNDates()
        self._cargo = UPNCargo()
        self._special_instructions = ""
        self._services = UPNServices()

    @property
    def references(self) -> UPNReferences:
        return self._references

    @references.setter
    def references(self, new_references: UPNReferences) -> None:
        if type(new_references) is not UPNReferences:
            raise TypeError("Incorrect type for references.")

        self._references = new_references

    @property
    def consignment_no(self) -> str:
        return self._references.consignment_no

    @property
    def barcode(self) -> str:
        return self._references.barcode

    @property
    def customer_reference(self) -> str:
        return self._references.customer_reference

    @property
    def depot_no(self) -> int:
        return self._depot_no

    @depot_no.setter
    def depot_no(self, new_depot_no: int) -> None:
        self._depot_no = new_depot_no

    @property
    def customer(self) -> UPNCustomer:
        return self._customer

    @customer.setter
    def customer(self, new_customer: UPNCustomer) -> None:
        if type(new_customer) is not UPNCustomer:
            raise TypeError("Incorrect type for customer.")

        self._customer = new_customer

    @property
    def customer_id(self) -> int:
        return self._customer.id

    @property
    def customer_name(self) -> str:
        return self._customer.name

    @property
    def dates(self) -> UPNDates:
        return self._dates

    @dates.setter
    def dates(self, new_dates: UPNDates) -> None:
        if type(new_dates) is not UPNDates:
            raise TypeError("Incorrect dates type.")

        self._dates = new_dates

    @property
    def despatch_date(self) -> datetime.datetime:
        return self._dates.despatch

    @property
    def delivery_datetime(self) -> datetime.datetime:
        return self._dates.delivery

    @property
    def delivery_address(self) -> UPNAddress:
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, new_address: UPNAddress) -> None:
        if type(new_address) is not UPNAddress:
            raise TypeError("Incorrect type for address.")

        self._delivery_address = new_address

    @property
    def delivery_name(self) -> str:
        return self._delivery_address.name

    @property
    def delivery_address_1(self) -> str:
        return self._delivery_address.line_1

    @property
    def delivery_address_2(self) -> str:
        return self._delivery_address.line_2

    @property
    def delivery_town(self) -> str:
        return self._delivery_address.town

    @property
    def delivery_county(self) -> str:
        return self._delivery_address.county

    @property
    def delivery_post_code(self) -> str:
        return self._delivery_address.post_code

    @property
    def delivery_telephone_no(self) -> str:
        return self._delivery_address.telephone_no

    @property
    def delivery_contact_name(self) -> str:
        return self._delivery_address.contact_name

    @property
    def delivery_country(self) -> str:
        return self._delivery_address.country

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

    @property
    def services(self) -> UPNServices:
        return self._services

    @services.setter
    def services(self, new_services: UPNServices) -> None:
        if type(new_services) is not UPNServices:
            raise TypeError("Incorrect type for services.")

        self._services = new_services

    @property
    def main_service(self) -> str:
        return self._services.main_service

    @property
    def premium_service(self) -> str:
        return self._services.premium_service

    @property
    def tail_lift_required(self) -> str:
        return self._services.tail_lift_required

    @property
    def additional_service(self) -> str:
        return self._services.additional_service

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, new_cargo) -> None:
        self._cargo = new_cargo

    @property
    def pallets(self) -> list[NetworkPallet]:
        return self._cargo.pallets

    @property
    def total_weight(self) -> int:
        return self._cargo.total_weight
