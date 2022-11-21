from src.main.upn.api.data_structures.network_pallet.structure \
    import NetworkPallet


def network_pallet() -> NetworkPallet:
    result = NetworkPallet()
    result.consignment_barcode = "W213359799C"
    result.pallet_size = "N"
    result.pallet_type = "FULL"
    result.barcode = "W213359800P"

    return result

