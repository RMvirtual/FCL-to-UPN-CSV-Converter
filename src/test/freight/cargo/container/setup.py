from src.main.freight.cargo.container.interface import Cargo as CargoInterface
from src.main.freight.cargo.container.implementation import Cargo
from src.main.freight.cargo.packages.types import factory
from src.main.freight.cargo.entries.implementation import CargoEntry


def two_entry_cargo() -> CargoInterface:
    result = Cargo()

    result.add(
        CargoEntry(package=factory.load("full"), quantity=3, weight=3000))

    result.add(
        CargoEntry(package=factory.load("half"), quantity=2, weight=1200))

    return result

