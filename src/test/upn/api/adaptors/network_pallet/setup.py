from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet


def full_normal_pallet() -> NetworkPallet:
    return _network_pallet("N", "FULL")


def double_half_pallet() -> NetworkPallet:
    return _network_pallet("2", "HALF")


def _network_pallet(pallet_size: str, pallet_type: str) -> NetworkPallet:
    result = NetworkPallet()
    result.consignment_barcode = "W213359799C"
    result.pallet_size = pallet_size
    result.pallet_type = pallet_type
    result.barcode = "W213359800P"

    return result
