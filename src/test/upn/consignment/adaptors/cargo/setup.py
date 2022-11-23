from src.main.graylaw.cargo.container.implementation import Cargo
from src.main.graylaw.cargo.entries.implementation import CargoEntry
from src.main.graylaw.cargo.packages.types import factory
from src.main.graylaw.cargo.container.interface import CargoReading
from src.main.upn.consignment.structures.cargo import UPNCargo

from src.main.upn.api.data_structures.network_pallet.implementation \
    import NetworkPallet


def single_entry_upn_cargo() -> UPNCargo:
    result = UPNCargo()
    result.total_weight = 3000
    network_pallet = NetworkPallet()
    network_pallet.consignment_barcode = "W123456789"
    network_pallet.barcode = "W987654321"
    network_pallet.size = "N"
    network_pallet.type = "FULL"

    for i in range(3):
        result.pallets.append(network_pallet)

    return result


def single_entry_cargo() -> CargoReading:
    result = Cargo()
    package_type = factory.load("full")
    entry = CargoEntry(package=package_type, quantity=3, weight=3000)
    result.add(entry)

    return result

