from src.main.graylaw.consignment.model import Consignment
from src.main.graylaw.address.implementation import Address
from src.main.graylaw.shipment_dates.implementation import ShipmentDates
from src.main.graylaw.cargo.container.implementation import Cargo
from src.main.graylaw.cargo.entries.implementation import CargoEntry
from src.main.graylaw.cargo.packages.types import factory


def dummy_consignment() -> Consignment:
    result = Consignment("GR221004388")
    result.client_name = "GRAYLAW FREIGHT GROUP"
    result.address = _address()
    result.cargo = _cargo()
    result.service.priority()
    result.shipment_dates = _dates()

    return result


def _address() -> Address:
    result = Address()
    result.name = "GRAYLAW FREIGHT GROUP"
    result.line_1 = "GRAYLAW FREIGHT TERMINAL"
    result.line_2 = "GILLBRANDS ROAD"
    result.town = "SKELMERSDALE"
    result.county = "LANCS"
    result.post_code = "WN8 9TA"
    result.country = "UNITED KINGDOM"
    result.contact_name = "Katherine   01695 729101"
    result.telephone_no = "0"

    return result


def _cargo() -> Cargo:
    result = Cargo()
    result.add(_cargo_entry())

    return result


def _cargo_entry() -> CargoEntry:
    return CargoEntry(factory.load("full"), 2, 650)


def _dates() -> ShipmentDates:
    result = ShipmentDates()
    result.collection_date = "18/10/2022"
    result.delivery_date = "18/10/2022"
    # result.delivery_time = "4:30"

    return result