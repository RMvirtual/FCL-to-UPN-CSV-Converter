import datetime
from src.main.upn.consignments.references import References
from src.main.upn.consignments.customer import Customer
from src.main.upn.consignments.cargo import Cargo
from src.main.upn.consignments.services import Services
from src.main.upn.consignments.dates import Dates
from src.main.upn.consignments.address import Address

from src.main.upn.api.data_structures.network_consignment.implementation \
    import NetworkConsignment

from src.main.upn.api.data_structures.network_pallet.implementation import \
    NetworkPallet


def dummy_network_consignment() -> NetworkConsignment:
    result = NetworkConsignment()
    result.references = _references()
    result.depot_no = 75
    result.customer_paperwork_pages = 0
    result.customer = _customer()
    result.delivery_address = _delivery_address()
    result.cargo = _cargo()
    result.dates = _dates()
    result.special_instructions = "Don't smash up this consignment."
    result.services = _services()

    return result


def _references() -> References:
    result = References()

    result.consignment_no = "GR221004388"
    result.customer_reference = "49632"
    result.barcode = "W213359799C"

    return result


def _delivery_address() -> Address:
    result = Address()
    result.name = "GRAYLAW FREIGHT GROUP"
    result.line_1 = "GRAYLAW FREIGHT TERMINAL"
    result.line_2 = "GILLBRANDS ROAD"
    result.town = "SKELMERSDALE"
    result.county = "LANCS"
    result.post_code = "WN8  9TA"
    result.country = "UNITED KINGDOM"
    result.contact_name = "Katherine   01695 729101"
    result.telephone_no = "0"

    return result


def _services() -> Services:
    result = Services()
    result.main_service = "P"
    result.premium_service = None
    result.tail_lift_required = None
    result.additional_service = None

    return result


def _cargo() -> Cargo:
    result = Cargo()
    result.total_weight = 1100
    result.pallets = _pallets()

    return result


def _customer() -> Customer:
    result = Customer()
    result.name = "GRAYLAW"
    result.id = 4236

    return result


def _dates() -> Dates:
    result = Dates()
    result.despatch = datetime.datetime(2022, 10, 18, 0, 0)
    result.delivery = datetime.datetime(2022, 10, 18, 16, 30)

    return result


def _pallets() -> list[NetworkPallet]:
    return [_network_pallet("W213359800P"), _network_pallet("W213359801P")]


def _network_pallet(barcode_no: str) -> NetworkPallet:
    result = NetworkPallet()
    result.consignment_barcode = "W213359799C"
    result.size = "N"
    result.type = "FULL"
    result.barcode = barcode_no

    return result
