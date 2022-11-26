from src.main.upn.packages.network_pallet import factory as pallet_factory
from src.main.upn.packages.network_pallet.interface \
    import NetworkPalletInterface

from src.main.metrics.dimensions.interface import Dimensions
from src.main.metrics.dimensions import factory as dims_factory

from src.main.graylaw.cargo.packages.oversize.options import (
    OversizeOption, OversizeOptions)


def normal_full_pallet() -> NetworkPalletInterface:
    result = pallet_factory.network_pallet(size_name="N", type_name="FULL")
    result.barcode = "W213359800P"
    result.consignment_barcode = "W213359799C"

    return result


def double_half_pallet() -> NetworkPalletInterface:
    result = pallet_factory.network_pallet(size_name="2", type_name="HALF")
    result.barcode = "W213359800P"
    result.consignment_barcode = "W213359799C"

    return result


def normal_full_max_dims() -> Dimensions:
    return dims_factory.dimensions_m3(1.2, 1.0, 2.0)


def double_half_max_dims() -> Dimensions:
    return dims_factory.dimensions_m3(1.2, 1.0, 1.0)


def oversize_values() -> OversizeOptions:
    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    return OversizeOptions(default=options[0], options=options)
