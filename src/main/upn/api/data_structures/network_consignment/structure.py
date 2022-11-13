import copy
import datetime

from src.main.upn.api.data_structures.network_consignment import interface
from src.main.upn.consignments.address import Address
from src.main.upn.consignments.references import References
from src.main.upn.consignments.services import Services
from src.main.upn.consignments.cargo import Cargo
from src.main.upn.consignments.customer import Customer
from src.main.upn.consignments.dates import Dates


class NetworkConsignment:
    def __init__(self):
        self._interface = interface.NetworkConsignmentInterface()
        self._references = References()
        self._depot_no = 75
        self._customer_paperwork_pages = 0
        self._customer = Customer()
        self._delivery_address = Address()
        self._dates = Dates()
        self._cargo = Cargo()
        self._special_instructions = ""
        self._services = Services()

    @property
    def delivery_address(self) -> Address:
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, new_address: Address) -> None:
        if type(new_address) is not Address:
            raise TypeError("Incorrect type for address.")

        self._delivery_address = new_address

    @property
    def references(self) -> References:
        return self._references

    @references.setter
    def references(self, new_references: References) -> None:
        if type(new_references) is not References:
            raise TypeError("Incorrect type for references.")

        self._references = new_references

    @property
    def services(self) -> Services:
        return self._services

    @services.setter
    def services(self, new_services: Services) -> None:
        if type(new_services) is not Services:
            raise TypeError("Incorrect type for services.")

        self._services = new_services

    @property
    def customer(self) -> int:
        return self._customer

    @customer.setter
    def customer(self, new_customer: Customer) -> None:
        if type(new_customer) is not Customer:
            raise TypeError("Incorrect type for customer.")

        self._customer = new_customer

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

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, new_cargo) -> None:
        self._cargo = new_cargo

    @property
    def dates(self) -> Dates:
        return self._dates

    @dates.setter
    def dates(self, new_dates: Dates) -> None:
        if type(new_dates) is not Dates:
            raise TypeError("Incorrect dates type.")

        self._dates = new_dates
