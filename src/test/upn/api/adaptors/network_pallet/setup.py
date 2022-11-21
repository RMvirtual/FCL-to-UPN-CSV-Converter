from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet

from src.main.graylaw.cargo.metrics.dimensions import (
    Dimensions, DimensionsInMetres)

from src.main.graylaw.cargo.packages.oversize.options import (
    OversizeOption, OversizeOptions)


def normal_full_pallet() -> NetworkPallet:
    return _network_pallet(pallet_size="N", pallet_type="FULL")


def normal_full_max_dims() -> Dimensions:
    return _dimensions(1.2, 1.0, 2.0)


def double_half_pallet() -> NetworkPallet:
    return _network_pallet(pallet_size="2", pallet_type="HALF")


def double_half_max_dims() -> Dimensions:
    return _dimensions(1.2, 1.0, 1.0)


def oversize_values() -> OversizeOptions:
    options = [
        OversizeOption("normal", 1.0), OversizeOption("oversize", 1.5),
        OversizeOption("double", 2.0), OversizeOption("triple", 3.0)
    ]

    return OversizeOptions(default=options[0], options=options)


def _network_pallet(pallet_size: str, pallet_type: str) -> NetworkPallet:
    result = NetworkPallet()
    result.consignment_barcode = "W213359799C"
    result.size = pallet_size
    result.type = pallet_type
    result.barcode = "W213359800P"

    return result


def _dimensions(length: float, width: float, height: float) -> Dimensions:
    result = DimensionsInMetres()
    result.length = length
    result.width = width
    result.height = height

    return result
